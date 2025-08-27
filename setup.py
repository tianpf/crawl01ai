from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="doubao-brand-mcp",
    version="1.0.0",
    author="Doubao MCP Team",
    author_email="support@example.com",
    description="豆包品牌信息MCP服务器 - 通过豆包平台获取品牌信息并生成行业评分",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tianpf/crawl01ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "doubao-mcp-server=doubao_mcp_server:main",
        ],
    },
    keywords="mcp, doubao, brand, analysis, scoring, ai",
    project_urls={
        "Bug Reports": "https://github.com/tianpf/crawl01ai/issues",
        "Source": "https://github.com/tianpf/crawl01ai",
        "Documentation": "https://github.com/tianpf/crawl01ai/blob/main/README.md",
    },
)