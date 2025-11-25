# Save your API key to track your progress and have access to the quantum computers
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

token = os.getenv("QISKIT_IBM_TOKEN")
channel = os.getenv("QISKIT_IBM_CHANNEL")
instance = os.getenv("QISKIT_IBM_INSTANCE")

from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService()
service.save_account(
    channel=channel,
    token=token,
    instance=instance,
    name="martin",
    overwrite=True
)