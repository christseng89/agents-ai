# Install WSL

## Install UV
```cmd
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
    uv 0.7.15
uvx --version
    uvx 0.7.15
mkdir projects
cd projects
git clone https://www.github.com/christseng89/agents-ai.git
uv sync
nano .env
# Add your .env variables here, or copy from .env_sample    
```
