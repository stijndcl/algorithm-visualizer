import argparse
from dataclasses import dataclass


@dataclass
class ArgsNamespace:
    """Namespace for the command-line arguments"""
    pass


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser"""
    parser = argparse.ArgumentParser()

    return parser
