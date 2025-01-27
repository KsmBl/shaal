# share directory in /shaal
# symlincs to directorys

# cli controll over symlincs

import subprocess
import sys

result = subprocess.run(['python3', '-m', 'http.server', '-d', '/shaal/'], capture_output=True, text=True, check=True)
print(result.stdout)
