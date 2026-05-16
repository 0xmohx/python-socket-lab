<<<<<<< HEAD
# python-socket-lab
Educational Python project demonstrating TCP client-server communication using sockets. It shows basic networking concepts, command exchange, and subprocess handling in a controlled local lab environment. For learning purposes only.
=======
# Python Socket Communication Lab

## 📌 Overview

This project is an educational Python-based lab that demonstrates the fundamentals of **TCP socket communication** using a simple client-server architecture.

It helps understand how networked applications communicate at a low level using Python’s built-in `socket` module.

---

## 🧠 Learning Objectives

This project focuses on:

- Understanding TCP/IP communication basics
- Building client-server architecture in Python
- Handling real-time data transmission using sockets
- Implementing multi-threaded connection handling
- Learning how data flows between systems over a network

---

## ⚙️ How It Works

### 🟢 Server
- Listens on a specific IP and port
- Accepts incoming client connections
- Receives messages from clients
- Processes and sends responses back
- Handles multiple clients using threading

### 🔵 Client
- Connects to the server using IP and port
- Sends messages over TCP connection
- Receives responses from the server
- Allows interactive communication

---

## 🔁 Communication Flow

Client → Server (message)  
Server → Processes request  
Server → Client (response)

---

## 🚀 How to Run the Project

### ⚠️ Important Requirement

You must open **two separate terminal windows** inside the **same project directory**:

- One for the server
- One for the client

Both must run at the same time.

---

## 📍 Step 1: Navigate to Project Folder

```bash id="step1"
cd python-socket-lab
▶️ Step 2: Start the Server

Run the server first:

python3 server.py --port 4444
What happens:
Server starts listening on port 4444
Waits for incoming client connections
Prints connected clients in terminal
💻 Step 3: Start the Client (New Terminal)

Open a second terminal in the same folder and run:

python3 client.py --host 127.0.0.1 --port 4444
What happens:
Client connects to the server
You can now type messages interactively
🔁 Step 4: Example Usage

Inside client terminal:

You: hello
Server: Server received: hello
🚪 Step 5: Exit Connection

To close the connection:

exit

Both client and server will safely close the session.

📂 Project Structure
server.py
client.py
README.md
requirements.txt
🧪 Technical Concepts Used
Python socket programming (TCP)
threading for handling multiple clients
Real-time communication (send/receive)
Basic client-server architecture
🧠 Security Perspective (Educational Context)

This project demonstrates the core communication primitive used in many real-world systems.

With further development, such structures can evolve into:

Remote administration systems (RAT concepts)
Reverse communication channels
Command execution environments in controlled labs

⚠️ This is strictly for educational purposes in safe lab environments only.

⚠️ Disclaimer

This project is created for educational and research purposes only.

Do not use this knowledge on unauthorized systems.

👨‍💻 Author

Cybersecurity Student / Pentesting Learning Path
>>>>>>> 7cbedd6 (Initial commit - socket lab project)
