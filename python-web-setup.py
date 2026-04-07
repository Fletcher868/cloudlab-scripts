#!/bin/bash
# python-web-setup.sh

set -e  # exit on error

PORT=${APP_PORT:-8000}
echo "🚀 Setting up Python Web Lab on port $PORT"

# Create a sample index.html
cat > index.html <<EOF
<!DOCTYPE html>
<html>
<head><title>CloudLab Python Server</title></head>
<body>
<h1>CloudLab Python Web Lab is running!</h1>
<p>Your private tunnel will be ready in a moment.</p>
</body>
</html>
EOF

# Start Python HTTP server in background
python3 -m http.server $PORT > app.log 2>&1 &

echo "✅ Python server started (PID $!)"
