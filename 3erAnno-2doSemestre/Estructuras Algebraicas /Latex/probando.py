import sys

def process_file(input_file, output_file):
    # Define LaTeX document header and footer
    latex_header = r"""\documentclass{article}

\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{mathpazo}
\usepackage{tcolorbox}
\usepackage[margin=0.8in]{geometry}
\usepackage[colorlinks=true]{hyperref}
\usepackage{tcolorbox}

\newtheoremstyle{break}
  {\topsep}{\topsep}% 
  {\itshape}{}% 
  {\bfseries}{}%
  {\newline}{}%
\theoremstyle{break}
\newtheorem{theorem}{Teorema}[section]
\newtheorem{corollary}{Corolario}[theorem]
\newtheorem{lemma}[theorem]{Lema}
\newtheorem{proposition}{Proposición}
\newtheorem*{remark}{Observación}
\newtheorem{definition}{Definición}[section]

\begin{document}

\title{1er Parcial Topología}
\author{Javier Vera}
\maketitle

"""

    latex_footer = r"\end{document}"

    # Open the input file and read its contents
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    inside_theorem = False
    inside_lemma = False
    inside_def = False
    inside_proof = False
    inside_coro = False
    inside_remark = False
    cleaned_lines = []

    # Add the LaTeX header to the cleaned lines
    cleaned_lines.append(latex_header)

    # Process each line
    for line in lines:
        # Remove all ">" characters
        line = line.replace('>', '')

        # Remove blockquote and mathematical brackets
        if '\\begin{blockquote}' in line or '\\end{blockquote}' in line or '\\[' in line or '\\]' in line:
            line = line.replace('\\begin{blockquote}', '').replace('\\end{blockquote}', '')
            line = line.replace('\\[', '').replace('\\]', '')

        # Remove words containing "^"
        line = ' '.join([word for word in line.split() if '^' not in word])

        # Replace "[!Theorem]" with "\begin{theorem}" and mark we're inside a theorem
        if '[!Theorem]' in line:
            line = line.replace('[!Theorem]', '\\begin{theorem}')
            inside_theorem = True

        if '[!Proof]' in line:
            line = line.replace('[!Proof]', '\\begin{proof}')
            inside_proof = True

        # Check if we've reached a blank line while inside a proof, and close it
        if inside_proof and line.strip() == '':
            cleaned_lines.append('\\end{proof}')
            inside_proof = False

        # Check if we've reached a blank line while inside a theorem, and close it
        if inside_theorem and line.strip() == '':
            cleaned_lines.append('\\end{theorem}')
            inside_theorem = False

        if '[!Remark]' in line:
            line = line.replace('[!Remark]', '\\begin{remark}')
            inside_remark = True

        if inside_remark and line.strip() == '':
            cleaned_lines.append('\\end{remark}')
            inside_remark = False

        if '[!Lemma]' in line:
            line = line.replace('[!Lemma]', '\\begin{lemma}')
            inside_lemma = True

        if inside_lemma and line.strip() == '':
            cleaned_lines.append('\\end{lemma}')
            inside_lemma = False

        if '[!Corollary]' in line:
            line = line.replace('[!Corollary]', '\\begin{corollary}')
            inside_coro = True

        if inside_coro and line.strip() == '':
            cleaned_lines.append('\\end{corollary}')
            inside_coro = False

        if '[!Definition]' in line:
            line = line.replace('[!Definition]', '\\begin{definition}')
            inside_def = True

        if inside_def and line.strip() == '':
            cleaned_lines.append('\\end{definition}')
            inside_def = False

        # Append the processed line
        cleaned_lines.append(line.rstrip())

    # Add the LaTeX footer to the cleaned lines
    cleaned_lines.append(latex_footer)

    # Write the cleaned lines to the output file
    with open(output_file, 'w') as file:
        file.write('\n'.join(cleaned_lines))

    print(f'Processed the text and saved the result to {output_file}')


if __name__ == "__main__":
    # Ensure we have the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    # Get the input and output file paths from the command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the function to process the file
    process_file(input_file, output_file)

