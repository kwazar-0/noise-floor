# Як використовувати ілюстрації як фон

## Концепція:

- **Прозорість:** 20% (opacity: 0.2)
- **Колір тексту:** підібраний під тон ілюстрації
- **Читабельність:** text-shadow для контрасту

---

## Використання:

### 1. Підключити новий CSS:

```html
<link rel="stylesheet" href="style-with-illustrations.css">
```

### 2. Додати class до body:

```html
<!-- Глава 1 -->
<body class="chapter-cell">

<!-- Глава 4 -->
<body class="chapter-karakul">

<!-- Глава 13 -->
<body class="chapter-mundshtuk">

<!-- Обкладинка / індекс -->
<body class="cover-page">
```

---

## Доступні classes:

### ЯДРО (1-17):
- `chapter-cell` — Ячейка
- `chapter-moskvich` — Москвич
- `chapter-dk` — ДК
- `chapter-karakul` — Каракуль
- `chapter-dossier` — Досьє
- `chapter-empty-place` — Пусте місце
- `chapter-dekanat` — Деканат
- `chapter-cafe` — Кафе комітету
- `chapter-garages` — Гаражі
- `chapter-sito` — СИТО
- `chapter-shulyavka` — Шулявка
- `chapter-grushevskogo` — Грушевського
- `chapter-mundshtuk` — Мундштук
- `chapter-koncha` — Конча
- `chapter-secret-court` — Таємний суд
- `chapter-zasov` — Засув
- `chapter-coda` — Кода

### ОРБІТА (18-25):
- `chapter-hawala` — Хавала
- `chapter-karina` — Каріна
- `chapter-vienna` — Відень
- `chapter-archive` — Архів
- `chapter-tzilya` — Ціля
- `chapter-tarik` — Тарік
- `chapter-lot47` — Лот 47
- `chapter-madam-lin` — Мадам Лінь

### СПЕЦІАЛЬНІ:
- `cover-page` — Обкладинка (для індексів)

---

## Автоматичний підбір кольору:

### Теплі глави (Салон Марго):
- `chapter-karakul`
- `chapter-mundshtuk`
- `chapter-dossier`
- **Колір тексту:** `#f5e6d3` (теплий крем)

### Холодні техно-глави (СИТО):
- `chapter-sito`
- `chapter-secret-court`
- **Колір тексту:** `#e0f0e0` (зелений відтінок)

### Інтелектуальні глави (Софія):
- `chapter-shulyavka`
- `chapter-archive`
- **Колір тексту:** `#e8e8f0` (холодний білий)

### Решта глав:
- **Колір тексту:** `#f5f5f5` (нейтральний світлий)

---

## Як працює:

PNG мають лежати **всередині `docs/`**, інакше GitHub Pages їх не віддає.

```css
/* Картинка на body, шлях від CSS-файла docs/style-with-illustrations.css */
body.character-nina {
    background-image: url('assets/references/characters/ref-character-nina.png');
}

/* 20% темна вуаль поверх фото */
body::before {
    background: rgba(10, 10, 10, 0.2);
}
```

---

## Приклад повної сторінки:

Див. `EXAMPLE-with-background.html`

---

## Швидке оновлення всіх сторінок:

```bash
# В кожному HTML файлі:
# 1. Змінити посилання на CSS
# 2. Додати відповідний class до <body>
```

**Або** використати script для автоматичної заміни:

```bash
cd docs/roman/01-orden-lipok/text/
# Для кожного glava-XX.html додати class
```
