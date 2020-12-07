import argparse

from molai import main


def cli():
    """Command Line Interface."""

    # Top-level parser:
    parser = argparse.ArgumentParser(prog="molai")
    subparsers = parser.add_subparsers(dest="command",
                                       help="command to be executed")

    # Parser for "train" command:
    train_parser = subparsers.add_parser("train", help="train a model")
    train_parser.add_argument("--model", help="model ID")

    # Parser for "evaluate" command:
    evaluate_parser = subparsers.add_parser("evaluate",
                                            help="evaluate a model")
    evaluate_parser.add_argument("--model", help="model ID")

    # Parser for "predict" command:
    predict_parser = subparsers.add_parser(
        "predict",
        help="use a model to predict the property 'P1' for a given smile"
    )
    predict_parser.add_argument("--smile", required=True,
                                help="molecule smile")
    predict_parser.add_argument("--model", help="model ID")

    # Parse args
    args = parser.parse_args()
    # Call function
    if args.command == "train":
        main.train(model_id=args.model)
    elif args.command == "evaluate":
        _ = main.evaluate(model_id=args.model)
    elif args.command == "predict":
        _ = main.predict(smile=args.smile, model_id=args.model)
        # print(f"Prediction = {prediction}")


if __name__ == "__main__":
    cli()
