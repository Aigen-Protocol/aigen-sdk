from setuptools import setup, find_packages

setup(
    name="aigen-tools",
    version="0.1.0",
    description="AIGEN SDK — Connect any AI agent to the AIGEN economy in 3 lines.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Aigen Protocol",
    author_email="contact@aigenprotocol.com",
    url="https://github.com/Aigen-Protocol/aigen-sdk",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["httpx>=0.24"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="aigen mcp ai-agents crypto web3",
    license="MIT",
)
