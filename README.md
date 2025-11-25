```
pip install 'qiskit[visualization]'
pip install qiskit-ibm-transpiler[ai-local-mode]
pip install qiskit_ibm_runtime
python login.py 
pip install dotenv
python transpiler_comparison.py
```

### Result
python transpiler_comparison.py 
We are using the ibm_torino quantum computer
AI Transpiler Results:
            ┌─────────┐┌─────────┐┌───┐┌─────────┐┌─────────┐           
 q_49 -> 80 ┤ Ry(0.3) ├┤ Rz(0.6) ├┤ X ├┤ Ry(0.9) ├┤ Rz(1.2) ├───────────
            ├─────────┤├─────────┤└─┬─┘└──┬───┬──┘├─────────┤┌─────────┐
q_115 -> 92 ┤ Ry(0.2) ├┤ Rz(0.5) ├──■─────┤ X ├───┤ Ry(0.8) ├┤ Rz(1.1) ├
            ├─────────┤├─────────┤        └─┬─┘   ├─────────┤└┬───────┬┘
 q_85 -> 99 ┤ Ry(0.1) ├┤ Rz(0.4) ├──────────■─────┤ Ry(0.7) ├─┤ Rz(1) ├─
            └─────────┘└─────────┘                └─────────┘ └───────┘ 
Time taken: 0.16684556007385254 seconds

Normal Transpiler Results:
     ┌─────────┐┌─────────┐ ░            ░ ┌─────────┐ ┌───────┐ 
q_0: ┤ Ry(0.1) ├┤ Rz(0.4) ├─░────────■───░─┤ Ry(0.7) ├─┤ Rz(1) ├─
     ├─────────┤├─────────┤ ░      ┌─┴─┐ ░ ├─────────┤┌┴───────┴┐
q_1: ┤ Ry(0.2) ├┤ Rz(0.5) ├─░───■──┤ X ├─░─┤ Ry(0.8) ├┤ Rz(1.1) ├
     ├─────────┤├─────────┤ ░ ┌─┴─┐└───┘ ░ ├─────────┤├─────────┤
q_2: ┤ Ry(0.3) ├┤ Rz(0.6) ├─░─┤ X ├──────░─┤ Ry(0.9) ├┤ Rz(1.2) ├
     └─────────┘└─────────┘ ░ └───┘      ░ └─────────┘└─────────┘
Time taken: 9.274482727050781e-05 seconds

Comparison of Results:
Gate count:
AI Transpiler: 3
Normal Transpiler: 4
Depth:
AI Transpiler: 6
Normal Transpiler: 6

![alt text](image.png)