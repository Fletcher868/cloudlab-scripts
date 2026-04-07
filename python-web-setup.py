print("🚀 Starting Python HTTP server...")

# Create a simple index.html
with open("index.html", "w") as f:
    f.write("""
    <html>
        <head><title>CloudLab Python Server</title></head>
        <body>
            <h1>✅ Your Python Web Lab is running!</h1>
            <p>This is a private instance.</p>
        </body>
    </html>
    """)

# Function to run the server
def run_server():
    os.system("python3 -m http.server 8000 > server.log 2>&1")

threading.Thread(target=run_server, daemon=True).start()
