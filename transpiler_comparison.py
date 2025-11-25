from qiskit.transpiler import PassManager
from qiskit.circuit.library import efficient_su2
from qiskit_ibm_transpiler.ai.routing import AIRouting
from qiskit_ibm_runtime import QiskitRuntimeService
import time
import matplotlib.pyplot as plt

# Define the backend
backend = QiskitRuntimeService().least_busy(operational=True, simulator=False)

# Define the AI pass manager
ai_passmanager = PassManager(
    [
        AIRouting(
            backend=backend,
            optimization_level=2,
            layout_mode="optimize",
            local_mode=True,
        )
    ]
)

# Define the normal pass manager
normal_passmanager = PassManager()

# Define the circuit parameters
num_qubits_list = [3, 5, 7, 10, 12, 15, 20]
reps_list = [1, 2, 3, 4, 5, 6, 7]

# Initialize lists to store results
ai_times = []
normal_times = []
ai_gate_counts = []
normal_gate_counts = []
ai_depths = []
normal_depths = []

for num_qubits in num_qubits_list:
    circuit = efficient_su2(num_qubits=num_qubits, reps=reps_list[num_qubits_list.index(num_qubits)], insert_barriers=True)
    params = list(circuit.parameters)

    # Create a list of random values that matches the number of parameters
    x = [0.1 * i for i in range(len(params))]

    encode = circuit.assign_parameters({param: value for param, value in zip(params, x)})

    # Transpile the circuit using the AI pass manager
    start_time = time.time()
    ai_transpiled_circuit = ai_passmanager.run(encode)
    ai_time = time.time() - start_time
    ai_times.append(ai_time)
    ai_gate_counts.append(len(ai_transpiled_circuit.count_ops()))
    ai_depths.append(ai_transpiled_circuit.depth())

    # Transpile the circuit using the normal pass manager
    start_time = time.time()
    normal_transpiled_circuit = normal_passmanager.run(encode)
    normal_time = time.time() - start_time
    normal_times.append(normal_time)
    normal_gate_counts.append(len(normal_transpiled_circuit.count_ops()))
    normal_depths.append(normal_transpiled_circuit.depth())

# Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(num_qubits_list, ai_times, label='AI Transpiler')
plt.plot(num_qubits_list, normal_times, label='Normal Transpiler')
plt.xlabel('Number of Qubits')
plt.ylabel('Time (seconds)')
plt.title('Transpilation Time')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(num_qubits_list, ai_gate_counts, label='AI Transpiler')
plt.plot(num_qubits_list, normal_gate_counts, label='Normal Transpiler')
plt.xlabel('Number of Qubits')
plt.ylabel('Gate Count')
plt.title('Gate Count')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(num_qubits_list, ai_depths, label='AI Transpiler')
plt.plot(num_qubits_list, normal_depths, label='Normal Transpiler')
plt.xlabel('Number of Qubits')
plt.ylabel('Depth')
plt.title('Circuit Depth')
plt.legend()

plt.tight_layout()
plt.savefig('image.png')