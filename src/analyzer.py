from .legacy_methods import calculate_engagement


def run_analysis():
    """Запуск анализа на основе методов из ВКР."""
    result = calculate_engagement("video_sample.mp4")
    print(f"Результат анализа вовлеченности: {result}")


if __name__ == "__main__":
    run_analysis()
