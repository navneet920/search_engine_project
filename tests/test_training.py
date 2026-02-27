from src.pipeline.training_pipeline import TrainingPipeline


if __name__ == "__main__":
    trainer = TrainingPipeline()
    trainer.run()

    print("Training completed successfully.")