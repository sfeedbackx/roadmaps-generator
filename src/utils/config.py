from dotenv import dotenv_values, load_dotenv
import sys
import os

script_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_path))
env_path = os.path.join(project_root, '.env')
config = dotenv_values(env_path)
load_dotenv(env_path)


def get_env_var(key):
	if key not in config.keys():
		raise Exception('Invalid Key')
	if len(config[key].strip()) == 0:
		raise Exception('Empty Value')
	return config[key].strip()


if __name__ == '__main__':
	arg = sys.argv[1]
	if arg is None:
		print('usage : python config.py key ')
		sys.exit(1)
	print(os.getenv(arg))
