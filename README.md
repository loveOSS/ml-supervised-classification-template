# ML App template

## How to get the dataset

@TODO

## Local installation

```bash
python -m venv dev
source dev/Scripts/activate
pip install -r requirements.txt
```

## Docker installation

### Build the image

```bash
docker build --tag app:1.0 .
```

### Access the REST API

```bash
docker run --publish 8501:8501 -it app:1.0 src/api.py
```

Then access [http://localhost:8501](http://localhost:8501/docs)

> Everytime you update the project, you must build a new image with a new tag.

## Train the model

1. Download the RAW data ;
2. Execute `src/clean.py` to create `cleaned_data.pkl` ;
3. Execute `src/feat_prep.py` to create `training.pkl` ;
4. Execute `src/create_folds.py` to create `training_folds.pkl` ;
5. Execute `src/train.py` to train the model ;

## Evaluate the performance of the model

```bash
python src/report.py --fold=1
```

> fold value is in range [0,4]

## Quality tools

```bash
python -m isort src/
python -m black src/
python -m flake8 src/ --count --statistics
```

## LICENSE

This project is provided under the MIT license.
