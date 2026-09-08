{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "f1ndr Backend (run_backend.py)",
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
            "name": "f1ndr Backend (package mode)",
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
