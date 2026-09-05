{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "F1NDR Backend (run_backend.py)",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/run_backend.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
        {
            "name": "F1NDR Backend (package mode)",
            "type": "python",
            "request": "launch",
            "module": "run_backend",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
        {
            "name": "Sellr (package mode)",
            "type": "python",
            "request": "launch",
            "module": "sellr.module",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
