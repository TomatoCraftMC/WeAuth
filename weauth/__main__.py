"""
Entrypoint for the weauth module
"""
from weauth import weauth_entrypoint


def main():
	return weauth_entrypoint.entrypoint()


if __name__ == '__main__':
	main()