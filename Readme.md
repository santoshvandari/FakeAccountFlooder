# Fake Account Generator for Scammer Website  

This Python script is designed to generate and register **fake accounts** on a scammer website that falsely claims to offer work opportunities in exchange for money. The goal of this script is to overwhelm the scammer's database by generating a large number of fake accounts, eventually leading to a system crash or making their database unusable.

---

## ⚠️ Disclaimer  

This script is provided for **educational purposes only**. Using this script to disrupt, damage, or compromise any system without the explicit permission of the system owner is **illegal** and could result in legal consequences. The author of this script does not support malicious activities and is not responsible for any misuse of this code. Use it responsibly and ethically!

---

## 🔧 Configuration  

If you need to change the target website or headers, modify the `URL` and `headers` inside the `post_request()` function in `main.py`:

```python
URL = "https://lerih3.cc/api/user/register"

headers = {
    "Host": "lerih3.cc",
    "Cookie": "think_lang=en-us; PHPSESSID=e5b98f7fff3342a73525130bb2d2b10d",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
    ...
}
```

---

## 🚀 Usage  

To run the script and start generating fake accounts, simply execute the script using the following command:
- Create the Virtual Environment (Not Necessary but Recommand) and activate it.
    ```bash
        # For Windows User
        python -m venv venv
        venv\Scripts\activate

        #For Linux User
        python3 -m virtualenv venv
        source venv/bin/activate

    ```
- Install the Requirements
    ```bash
        pip install -r requirements.txt
    ```
- Run the `main.py` file

    ```bash
    python main.py
    ```

The script will continuously generate random fake accounts and send them to the target website.

---

## 💡 How It Works  

1. **Random Data Generation**:  
   The script uses the `Faker` library as well as custom function to generate random user data, including usernames, mobile numbers, passwords, and machine IDs.

2. **Data Encoding**:  
   The generated data is first converted to a JSON string, URL-encoded, and then Base64-encoded to match the server's expected format.

3. **HTTP Request**:  
   The encoded data is sent to the scammer's API endpoint using a POST request with appropriate headers to mimic a legitimate user.

4. **Continuous Execution**:  
   The script can run indefinitely, continuously sending fake account registrations to overload the scammer's system.

---

## 🧩 Example Output  

```bash
Account Count: 1
Response Code: 1, Response Message: Registration success
Account Count: 2
Response Code: 2, Response Message: Missing Invatation Code
Account Count: 3
Response Code: 1, Response Message: Registration success
Account Count: 4
Response Code: 2, Response Message: Internal Server Error.
Account Count: 5
Response Code: 1, Response Message: Registration success
```

---

## 🎯 Objectives  

- **Flood the scammer's database** with thousands of fake accounts.
- **Disrupt** their operations by consuming server resources.
- **Overwhelm** their system to reduce their ability to scam unsuspecting victims.

---

## 📌 Important Notes  

- The script does not store any data locally or create persistent accounts.  
- The target website might implement rate limiting or other countermeasures. Use appropriate methods to bypass such restrictions if necessary (e.g., rotating IP addresses with proxies).  
- Be aware that the target may log incoming requests and take actions against your IP address.

---

## 🔒 Legal Disclaimer  

Using this script to target websites without proper authorization is illegal and unethical. You are responsible for your actions when using this script. The author and contributors are not liable for any damages or legal actions resulting from the misuse of this script.

---

## 💬 **Contributing**  

We welcome contributions! Feel free to submit a pull request or open an issue if you encounter bugs or have ideas for new features.

---

## 📜 **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 **Contact**  

For inquiries or support, feel free to reach out:  
- **GitHub**: [@santoshvandari](https://github.com/santoshvandari)  

---
