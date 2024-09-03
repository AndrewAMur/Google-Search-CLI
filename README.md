# Google Search CLI

Google Search CLI is a Python application that lets you search the web using Google Search Engine directly from your terminal. It leverages the Serp API to fetch search results.

## Getting Started

Follow these steps to set up and run the project:

### Cloning the Repository

Clone the repository with:

```bash
git clone https://github.com/AndrewAMur/Google-Search-CLI.git
cd Google-Search-CLI
```

### Setting Up the Environment

1. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Serp API Key**:
    Create a `.env` file in the root directory (the same location as `main.py`) and add your Serp API key:
    ```
    api_key=[your serp api key here]
    ```

### Running the Program

Execute the following command to start the program:

```bash
python main.py
```

### Contributing

I welcome contributions to improve the Google Search CLI! To get started:

1. **Fork the Repository**: Click on the "Fork" button at the top right of this page.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/[your-username]/Google-Search-CLI.git
    cd Google-Search-CLI
    ```
3. **Create a New Branch**:
    ```bash
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**: Edit or add new files as needed.
5. **Commit Your Changes**:
    ```bash
    git add .
    git commit -m "Describe your changes"
    ```
6. **Push to Your Fork**:
    ```bash
    git push origin your-branch-name
    ```
7. **Create a Pull Request**: Go to the "Pull Requests" tab on GitHub and click "New Pull Request".

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/AndrewAMur/Google-Search-CLI/issues).
