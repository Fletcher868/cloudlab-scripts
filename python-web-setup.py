#!/bin/bash
# This script runs in the Colab environment.
# It must start the application on the given port and then exit (or run in background).

echo "🚀 Starting Python HTTP server on port 8000..."
cat > index.html <<EOF
<h1>CloudLab Python Server Live!</h1>
<p>Your private lab is ready.</p>
EOF

# Run the server in the background
python3 -m http.server 8000 > app.log 2>&1 &

# Give it a moment to bind
sleep 2
echo "✅ Server started"
