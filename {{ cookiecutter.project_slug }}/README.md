# {{ cookiecutter.project_name }}

## How to run

1. Make virtual environment and activate it

    ```shell
    python3 -m venv venv
    . venv/bin/activate
    ```

2. Install dependencies

    ```shell
    pip install -r requirements/local.txt
    ```

3. Build .env file

    ```shell
    cd scripts
    ./mkenv.sh
    ```

4. Run the project

    ```shell
    cd ..
    ./run.py
    ```
