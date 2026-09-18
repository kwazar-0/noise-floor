#!/usr/bin/env python3
"""
Convert markdown chapters to HTML for GitHub Pages
"""

import os
import re
from pathlib import Path
from typing import Optional

# Markdown to HTML simple converter (no external deps)
def markdown_to_html(text: str) -> str:
    """Convert markdown to HTML with basic formatting"""
    
    # Headers
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Bold and italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'«(.+?)»', r'«\1»', text)  # Keep quotes
    
    # Blockquotes
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)
    
    # Code blocks
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    
    # Horizontal rules
    text = re.sub(r'^---$', r'<hr>', text, flags=re.MULTILINE)
    
    # Paragraphs (lines separated by blank lines)
    paragraphs = []
    current_para = []
    
    for line in text.split('\n'):
        line = line.strip()
        
        # Skip if already HTML tag
        if line.startswith('<') or not line:
            if current_para:
                para_text = ' '.join(current_para)
                if not para_text.startswith('<'):
                    paragraphs.append(f'<p>{para_text}</p>')
                else:
                    paragraphs.append(para_text)
                current_para = []
            if line:
                paragraphs.append(line)
        else:
            current_para.append(line)
    
    if current_para:
        para_text = ' '.join(current_para)
        if not para_text.startswith('<'):
            paragraphs.append(f'<p>{para_text}</p>')
        else:
            paragraphs.append(para_text)
    
    return '\n\n'.join(paragraphs)


def create_html_page(
    title: str,
    content: str,
    tome_num: int,
    tome_name: str,
    prev_link: Optional[str] = None,
    next_link: Optional[str] = None,
    index_link: str = "index.html"
) -> str:
    """Create full HTML page with navigation"""
    
    css_path = "../style.css" if tome_num == 0 else "../../style.css"
    
    nav_links = []
    if prev_link:
        nav_links.append(f'<a href="{prev_link}">← Назад</a>')
    nav_links.append(f'<a href="{index_link}">К оглавлению</a>')
    if next_link:
        nav_links.append(f'<a href="{next_link}">Вперёд →</a>')
    
    navigation = ' | '.join(nav_links)
    
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — {tome_name}</title>
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
    <p>{navigation}</p>

    <article>
{content}
    </article>

    <hr>

    <p class="metadata">{navigation}</p>

</body>
</html>"""
    
    return html


def convert_tome(tome_num: int, tome_path: str, tome_name: str, output_path: str):
    """Convert all chapters from a tome"""
    
    text_dir = Path(tome_path) / "text"
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get list of chapter files
    if tome_num == 1:
        # Tom 1: prolog + glava-01 to glava-27 (skip OLD/backup files)
        files = []
        if (text_dir / "prolog.md").exists():
            files.append("prolog.md")
        
        # Get all glava-*.md files, excluding OLD/backup
        all_md = sorted(text_dir.glob("glava-*.md"))
        for file_path in all_md:
            filename = file_path.name
            # Skip OLD, backup, and NEW versions
            if any(x in filename for x in ['-OLD', '-old', '-NEW', '-new', 'backup']):
                continue
            files.append(filename)
    
    elif tome_num == 2:
        # Tom 2: prolog, sessions, intermedia, epilog
        files = []
        if (text_dir / "prolog.md").exists():
            files.append("prolog.md")
        
        # Sessions 1-4
        for i in range(1, 5):
            if i < 4:
                fname = f"session-{i:02d}.md"
            else:
                fname = "session-04-genesis.md"
            if (text_dir / fname).exists():
                files.append(fname)
        
        # Intermedia
        for i in range(1, 5):
            intermedia_files = [
                "intermedia-01-senator.md",
                "intermedia-02-mark.md",
                "intermedia-03-artur.md",
                "intermedia-04-final.md"
            ]
            if (text_dir / intermedia_files[i-1]).exists():
                files.append(intermedia_files[i-1])
        
        if (text_dir / "epilog.md").exists():
            files.append("epilog.md")
    
    elif tome_num == 3:
        # Tom 3: akt-01 to akt-16
        files = []
        for i in range(1, 17):
            tracks = ["manhattan", "baltic", "channel", "bellingcat"]
            block = (i - 1) // 4 + 1
            track = tracks[(i - 1) % 4]
            fname = f"akt-{i:02d}-{track}-{['i', 'ii', 'iii', 'iv'][block-1]}.md"
            if (text_dir / fname).exists():
                files.append(fname)
    
    else:
        return
    
    print(f"Converting Том {tome_num}: {len(files)} files")
    
    # Convert each file
    for idx, filename in enumerate(files):
        input_file = text_dir / filename
        output_file = output_dir / filename.replace('.md', '.html')
        
        # Read markdown
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        except Exception as e:
            print(f"  ⚠️  Error reading {filename}: {e}")
            continue
        
        # Extract title from first line or filename
        first_line = markdown_content.split('\n')[0]
        if first_line.startswith('#'):
            title = first_line.lstrip('#').strip()
        else:
            title = filename.replace('.md', '').replace('-', ' ').title()
        
        # Convert to HTML
        html_content = markdown_to_html(markdown_content)
        
        # Determine prev/next links
        prev_link = None
        next_link = None
        
        if idx > 0:
            prev_link = files[idx - 1].replace('.md', '.html')
        if idx < len(files) - 1:
            next_link = files[idx + 1].replace('.md', '.html')
        
        # Create full HTML page
        full_html = create_html_page(
            title=title,
            content=html_content,
            tome_num=tome_num,
            tome_name=tome_name,
            prev_link=prev_link,
            next_link=next_link,
            index_link="../index.html" if tome_num == 0 else "index.html"
        )
        
        # Write HTML file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"  ✓ {filename} → {output_file.name}")
        except Exception as e:
            print(f"  ⚠️  Error writing {output_file}: {e}")


def main():
    """Main conversion function"""
    
    base_dir = Path(__file__).parent.parent
    roman_dir = base_dir / "roman"
    docs_dir = base_dir / "docs"
    
    print("=" * 60)
    print("Converting Markdown to HTML for GitHub Pages")
    print("=" * 60)
    
    # Tom 1
    convert_tome(
        tome_num=1,
        tome_path=str(roman_dir / "01-orden-lipok"),
        tome_name="Орден Липок",
        output_path=str(docs_dir / "01-orden-lipok")
    )
    
    # Tom 2
    convert_tome(
        tome_num=2,
        tome_path=str(roman_dir / "02-nulevoj-blok"),
        tome_name="Нулевой блок",
        output_path=str(docs_dir / "02-nulevoj-blok")
    )
    
    # Tom 3
    convert_tome(
        tome_num=3,
        tome_path=str(roman_dir / "03-nizhe-urovnya-shuma"),
        tome_name="Ниже уровня шума",
        output_path=str(docs_dir / "03-nizhe-urovnya-shuma")
    )
    
    print("=" * 60)
    print("✓ Conversion complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
