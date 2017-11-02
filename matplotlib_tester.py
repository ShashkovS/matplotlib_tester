# -*- coding: utf-8 -*-
def print_ax(ax, lines=True, title=True, axis_labels=True, plot_labes=True):
    # Проверяем, что холст существует
    if 'Axes' not in ax.__class__.__name__:
        print('Переменная ax задана неверно. Должна быть команда вида `fig, ax = plt.subplots()`.')
        return
    if lines:
        # Находим все линии
        lines = [line._xy.round(2) for line in ax.lines]
        # Проверяем, сколько на нём линий
        print('На холсте ax найдено {} линий.'.format(len(lines)))
        # Выводим линии
        for i, line in enumerate(lines, start=1):
            print('*'*12 + str(i).center(7) + '*'*12)
            for j, (x, y) in enumerate(line):
                print('Л.{},т.{:03}: ({:+7.2f},{:+7.2f})'.format(i, j, x, y))
    if title:
        print('Заголовок:', ax.title._text)
    if axis_labels:
        print('Подпись оси x:', ax._axes.xaxis.label._text)
        print('Подпись оси y:', ax._axes.yaxis.label._text)
    if plot_labes:
        for i, line in enumerate(ax.lines, start=1):
            print('Подписи линии {}: {}'.format(i, repr(line._label)))
