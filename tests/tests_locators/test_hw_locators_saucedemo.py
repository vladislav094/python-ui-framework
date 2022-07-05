import logging

logger = logging.getLogger()
print(logger)


def main(name):
	logger.warning(f"Enter in the main() function: name = {name}")

if __name__ == "__main__":
	main('Oleg')