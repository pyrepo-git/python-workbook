#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
Перед тобой снова составляющие баг репорта.
В коде даны два списка priority и severity.
Значения в них перепутаны.
Твоя задача скорректировать списки.
"""

priority = ["Значительный", "Средний", "Тривиальный"]
severity = [
    "Низкий",
    "Незначительный",
    "Блокирующий",
    "Высокий",
    "Критический",
]


def sort_priority(element: str) -> int:
    if element == "Высокий":
        return 0
    if element == "Средний":
        return 1
    if element == "Низкий":
        return 2
    return 100


def sort_severity(element: str) -> int:
    if element == "Блокирующий":
        return 0
    if element == "Критический":
        return 1
    if element == "Значительный":
        return 2
    if element == "Незначительный":
        return 3
    if element == "Тривиальный":
        return 4
    return 100


def work() -> None:
    temporary = priority + severity
    priority_res = [
        x
        for x in temporary
        if x == "Высокий" or x == "Средний" or x == "Низкий"
    ]
    priority_res.sort(key=sort_priority)

    severity_res = [
        x
        for x in temporary
        if x == "Блокирующий"
        or x == "Критический"
        or x == "Значительный"
        or x == "Незначительный"
        or x == "Тривиальный"
    ]
    severity_res.sort(key=sort_severity)

    print(priority_res)
    print(severity_res)


def main() -> None:
    work()


if __name__ == "__main__":
    main()
