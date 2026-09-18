# Библия кадра — Том 01

**Фаза A.** Общий актив манги, дорамы и Pages.  
Lock: `roman/01-orden-lipok/CANON-LOCK.md`  
Stop-list: `roman/00-cikl/setings/adaptaciya/stop-list.md`  
Карта глав: `roman/01-orden-lipok/export/CHAPTER-MAP.md`

Пить **отсюда**, не из `export/izdanie/` и не из имён `tom1-v2-01-cell`.

Стиль: noir realism, зерно, 1992, европейские лица. Не anime.

---

## Lookbook Оли (том 01 = стадии 1–5)

Стадия **6** (`ref-olya-06-businesswoman.png`) — том 02. В ячейку и на Липки 92-го не ставить.

| Стадия | Файл | Главы | Запрет |
|---|---|---|---|
| 1 Студентка | `references/characters/ref-olya-01-student.png` | **1** (общага), вход в 2 | не салон |
| 2 Адептка | `ref-olya-02-cult-adept.png` | **2–3** (пять ночей) | не гл. 1; не лагерь; не `_deprecated` v1 |
| 3 Начало у Марго | `ref-olya-03-training-start.png` | **5, 7–8** | соло, без «молодой Марго» в кадре |
| 4 «Донечка» ВП | `ref-olya-04-vp-daughter.png` | **14, 16** | не культ |
| 5 Референт | `ref-olya-05-mink-vaz2108.png` (гл. 9, філфак) / `ref-olya-05-government-referent.png` (коридор) | **9, 12, 14+** | норка = чужой скафандр; не KPI; не ст. 6 |

Лицо одно. Меняются ткань, спина, свет.

---

## Лица (новые листы фазы A)

Все в `assets/references/characters/`.

| Кто | Файл | Правило |
|---|---|---|
| Вчитель | `ref-character-teacher-silhouette.png` | **лица нет** (спина, кисти, проём) |
| Іса | `ref-character-isa.png` | сбоку зеркала, папірець, не цирк |
| Саня | `ref-character-sanya.png` | дешёвий шкіряк; золотий рот не гриль |
| Сідий | `ref-character-sedoy.png` | цегла-телефон, не малиновий піджак |
| Артур (Київ) | `ref-character-artur-kyiv.png` | не Vance тома 03 |
| Поліна | `ref-character-polina.png` | перли молодші за Софьїні |
| Варяг | `ref-character-varyag.png` | кирза, ключі, коньяк не залпом |
| Циля | `ref-character-tsilya.png` | лупа, кардиган, Яффо |
| Лінь | `ref-character-madam-lin.png` | **єдине ципао** |

Уже канон v2: Марго aristocratic, Софья british, Ніна, Інженер, Віктор.

---

## Інтер'єри (нові)

`assets/references/interiors/`

| Місце | Файл | Глава |
|---|---|---|
| Общага | `ref-interior-dorm-glava01.png` | 1 (не ячейка) |
| Ячейка (гурток) | `ref-interior-cult-cell-club.png` | **2** (не барак `ref-interior-cult-cell.png`) |
| Деканат | `ref-interior-dekanat.png` | **9** — порожній кабінет |
| Деканат (Pages) | `scenes/ref-scene-09-dean-sees-fox.png` | **9** — фон читалки: Ірина Петрівна / Оля в песці |
| Стійка / школа | `ref-interior-training-dawn.png` | **7** |
| Гримёрка ДК | `ref-interior-dk-dressing-room.png` | 5 |
| Салон «Москвича» | `ref-interior-moskvich.png` | 4 |
| «Захер» | `ref-interior-sacher.png` | епілог |

Салон Марго / стійка / СИТО / Софья / дача Віктора — як у `references/README.md`, без `_deprecated`.

---

## Hero props

`assets/references/props/`

| Речі | Файл | KV |
|---|---|---|
| Трубка | `ref-prop-receiver.png` | гл. 1 / еп. 1 |
| Аркуш | `ref-prop-address-sheet.png` | гл. 1 |
| Капсула в кулаці | `ref-prop-capsule-fist.png` | гл. 3 |
| Студентський | `ref-prop-student-id.png` | 1–5; **СТУДЕНТСЬКИЙ КВИТОК**, філфак Шевченка; не КПІ; не «СТУДЕНЧЕСКИЙ КВИТОК» |
| Мундштук | `ref-prop-mouthpiece.png` | Марго |
| Монета | `ref-prop-coin.png` | Інженер; **царський** двоглавий орел, не герб України |
| Гайвань | `ref-prop-gaiwan.png` | гл. 27 |
| Три аркуші | `ref-prop-contract-three-sheets.png` | гл. 8 |

---

## Ілюстрації глав — канонічні імена

Старі файли `illustrations/tom1-v2/tom1-v2-NN-*.png` **не видаляти** (CSS Pages).  
Правильні номери: `illustrations/tom1-canon/chNN-*.png`

`tom1-v2-01-cell` = **глава 2**, не 1.

Повний рядок — `roman/01-orden-lipok/export/CHAPTER-MAP.md`.

Pages: класи `body` вирівняні під lock. Гл. 1 лишається `character-nina`. Гл. 8 — `chapter-contract` (три аркуші).

---

## Як генерувати новий кадр

1. Взяти lock + stop-list.
2. Оля — стадія з таблиці вище.
3. `reference_image_paths`: особа + інтер'єр + prop.
4. Не підписувати формулами інституту на картинці.

**Виход фазы A:** ця папка. Далі фаза B — перешити `dorama/` і `izdanie/`.
