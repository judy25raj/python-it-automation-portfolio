# ws01 Debug Report – HTTP 500 on Cloud Web Server

## 1. Summary

The cloud web server **ws01** was returning **HTTP 500 – Internal Server Error**.
Root cause was a **port conflict on TCP port 80** between the production
Apache web server (`apache2`) and a developer test script (`jimmytest.py`)
running under a systemd service. Disabling the test service and restarting
Apache resolved the issue.

---

## 2. Symptoms

- End users reported that the website hosted on `ws01` was unavailable.
- Accessing `http://<ws01-external-ip>/` returned:
  - `500 Internal Server Error`
- `systemctl status apache2` showed:
  - `Active: failed`
  - Error lines like:
    - `Address already in use: AH00072: make_sock: could not bind to address [::]:80`
    - `Unable to open logs`

---

## 3. Investigation Steps

1. **Checked Apache status**

   ```bash
   sudo systemctl status apache2
   ```

   - Service in `failed` state.
   - Log output mentioned inability to bind to port 80.

2. **Verified port usage**

   ```bash
   sudo netstat -nlp
   ```

   - Saw `python3` listening on `0.0.0.0:80`:
     - `tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN 1356/python3`

3. **Identified the Python process**

   ```bash
   ps -ax | grep python3
   ```

   - Found:
     - `python3 /usr/local/bin/jimmytest.py`
   - This indicated a developer test script using the production web port.

4. **Attempted to kill the process**

   ```bash
   sudo kill <PID>
   ps -ax | grep python3
   ```

   - The process reappeared with a new PID → likely managed by `systemd`.

5. **Searched for a related systemd service**

   ```bash
   sudo systemctl --type=service | grep jimmy
   ```

   - Found:
     - `jimmytest.service loaded active running Jimmy python test service`

---

## 4. Root Cause

- A `systemd` service (`jimmytest.service`) was configured to:
  - Start and keep running `/usr/local/bin/jimmytest.py`.
- This Python script was **binding to port 80**, which is reserved for the
  main Apache web server.
- As a result:
  - Apache could not start (`Address already in use`).
  - The site returned HTTP 500 errors when accessed.

---

## 5. Fix Implemented

1. Stopped and disabled the rogue systemd service:

   ```bash
   sudo systemctl stop jimmytest
   sudo systemctl disable jimmytest
   ```

2. Confirmed that no process was using port 80:

   ```bash
   sudo netstat -nlp | grep ':80 ' || echo "No process on port 80"
   ```

3. Restarted Apache:

   ```bash
   sudo systemctl start apache2
   sudo systemctl status apache2
   ```

4. Verified in the browser that:
   - `http://<ws01-external-ip>/` served the **Apache2 Ubuntu Default Page**.

---

## 6. Preventive Measures

- **Change process ports** for developer test scripts:
  - Require non-production apps to use high, non-standard ports (e.g. 8080, 5000).
- **Review systemd service definitions**:
  - Ensure only approved services are enabled on production servers.
- **Implement change control**:
  - Require a review before new services are added to production.
- **Add monitoring/alerts**:
  - Detect `apache2` service failures.
  - Alert when key ports (like 80/443) are not owned by expected processes.

---

## 7. Talking Point for Portfolio / Interviews

> I diagnosed an HTTP 500 issue on a cloud-hosted Apache server by
> systematically checking service status and network ports. Using `systemctl`,
> `netstat`, and `ps`, I traced the problem to a developer test script
> (`jimmytest.py`) running as a systemd service and binding to port 80.
> After disabling the test service and restarting Apache, the production
> website returned to a healthy state. This exercise demonstrates my ability
> to debug Linux services, understand port conflicts, and restore availability
> under time pressure.
