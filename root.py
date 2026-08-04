from dotenv import load_dotenv
import kagglehub

load_dotenv()

path = kagglehub.dataset_download("ismetsemedov/transactions")

print("Path to dataset files:", path)
