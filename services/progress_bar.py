import time
from datetime import timedelta


class ProgressBar:
    """Класс для отображения прогресс-бара с оценкой времени"""

    def __init__(self, total, prefix='Прогресс', length=50, fill='█', empty='░'):
        """
        total : int - общее количество итераций
        prefix : str - текст перед баром
        length : int - длина бара в символах
        fill : str - символ заполнения
        empty : str - символ пустоты
        """
        self.total = total
        self.prefix = prefix
        self.length = length
        self.fill = fill
        self.empty = empty
        self.start_time = time.time()
        self.current = 0

    def update(self, current=None, step=1):
        """Обновляет прогресс-бар"""
        if current is not None:
            self.current = current
        else:
            self.current += step

        # Расчет процентов
        percent = 100 * (self.current / float(self.total))

        # Расчет времени
        elapsed = time.time() - self.start_time
        if self.current > 0:
            eta = (elapsed / self.current) * (self.total - self.current)
        else:
            eta = 0

        # Форматирование времени
        elapsed_str = str(timedelta(seconds=int(elapsed)))
        eta_str = str(timedelta(seconds=int(eta)))

        # Создание полосы прогресса
        filled_length = int(self.length * self.current // self.total)
        bar = self.fill * filled_length + self.empty * (self.length - filled_length)

        # Вывод
        print(f'\r{self.prefix} |{bar}| {percent:.1f}% | '
              f'[{self.current}/{self.total}] | '
              f'Прошло: {elapsed_str} | Осталось: {eta_str}', end='')

        if self.current == self.total:
            print()

    def finish(self):
        """Завершает прогресс-бар"""
        self.update(self.total)
        print(f"\n✅ {self.prefix} завершен за {str(timedelta(seconds=int(time.time() - self.start_time)))}")
