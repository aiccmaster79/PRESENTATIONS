#!/usr/bin/env python3
"""Generate Microsoft Forms Quick Import PDFs for deck #141 VEX Base Bot.

Usage:
  python3 quizzes/generate_vex_forms_quiz.py

Outputs:
  quizzes/vex-base-bot-forms-quiz.pdf          (upload this to Forms as Quiz)
  quizzes/vex-base-bot-forms-quiz-answer-key.pdf
"""

from pathlib import Path

from fpdf import FPDF

OUT_DIR = Path(__file__).resolve().parent

QUESTIONS = [
    (
        "What is the main controller on a VEX Base Bot?",
        [
            "V5 Brain",
            "Wireless remote only",
            "Arduino microcontroller",
            "Raspberry Pi",
        ],
        "A",
        "The V5 Brain runs the program and drives ports.",
    ),
    (
        "Which environment is used to program VEX robots?",
        [
            "Only block-based coding",
            "VEXcode with Blocks or C++ options",
            "Python exclusively",
            "Hardware assembly only",
        ],
        "B",
        "VEXcode supports Blocks and text (C++); both upload to the Brain.",
    ),
    (
        "What do rotation sensors (encoders) measure on the Base Bot?",
        [
            "How far a wheel or motor has turned",
            "The temperature of motors",
            "The wireless signal strength",
            "Battery voltage only",
        ],
        "A",
        "Encoders count turns so distance can be measured in autonomous.",
    ),
    (
        "Both drive sides are set to 50% but the bot pulls left. What should you check first?",
        [
            "Rewrite the entire autonomous routine",
            "Left motor cable, port, and wheel bind",
            "Buy a new V5 Brain immediately",
            "Disable all sensors",
        ],
        "B",
        "Identical commands still curve if a cable is loose or a wheel binds.",
    ),
    (
        "Autonomous stops early every run. The distance sensor faces the floor. Likely cause?",
        [
            "The battery is empty",
            "The stop condition is reading the floor",
            "VEXcode cannot run autonomous",
            "The radio must be unplugged",
        ],
        "B",
        "A floor-facing distance sensor triggers the stop condition early.",
    ),
    (
        "Why should the Brain and battery be centred on the chassis?",
        [
            "It looks neater in photos",
            "A lower, centred mass improves stability",
            "Sensors only work at the rear",
            "Wireless range doubles",
        ],
        "B",
        "Centred mass reduces tipping and curved turns.",
    ),
    (
        "In the Base Bot control stack, which layer runs the program?",
        [
            "Drive motors",
            "V5 Brain",
            "Distance sensor",
            "Wheel tyres",
        ],
        "B",
        "Only the Brain executes the uploaded program.",
    ),
    (
        "What is differential steering on a Base Bot?",
        [
            "Turning by running left and right sides at different speeds",
            "Using only one motor for all movement",
            "Steering with a car-style front axle only",
            "Turning only when the battery is low",
        ],
        "A",
        "Left/right speed difference turns the drivetrain.",
    ),
    (
        "Autonomous mode means:",
        [
            "A student drives with the controller in real time",
            "The robot follows pre-programmed instructions without live driver input",
            "The robot cannot use sensors",
            "The Brain is switched off",
        ],
        "B",
        "Autonomous uses pre-written code without live driver input.",
    ),
    (
        "A gear ratio that increases torque usually:",
        [
            "Also increases top speed",
            "Reduces top speed on long runs",
            "Removes the need for a battery",
            "Disables encoder feedback",
        ],
        "B",
        "More torque usually means less top speed.",
    ),
    (
        "Before rewriting code for a skills match, which check comes first?",
        [
            "Confirm autonomous and driver programs are downloaded and selected on the Brain",
            "Change motor power randomly",
            "Remove all sensors from the bot",
            "Delete the driver-control program",
        ],
        "A",
        "Confirm program slots before rewriting code.",
    ),
    (
        "Low battery on a Base Bot often looks like:",
        [
            "Stronger wireless range",
            "Weak or inconsistent motor drive",
            "Faster autonomous scoring",
            "Automatic sensor calibration",
        ],
        "B",
        "Low voltage often shows up as weak or inconsistent motors.",
    ),
]

OPEN = [
    "In one or two sentences, explain why you should check motor cables before rewriting a drive program.",
    "Name two sensors used on a Base Bot and state what each one measures.",
]

LETTERS = "ABCD"


class QuizPDF(FPDF):
    def __init__(self, footer_label: str):
        super().__init__(format="A4")
        self.footer_label = footer_label

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            8,
            f"Page {self.page_no()}/{{nb}}  |  {self.footer_label}",
            align="C",
        )

    def write_block(self, text, size=11, style="", color=(20, 22, 26), lh=6):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", style, size)
        self.set_text_color(*color)
        self.multi_cell(self.epw, lh, text)


def build_forms_quiz() -> Path:
    pdf = QuizPDF("OCN NI #141 VEX Base Bot | Forms Quick Import")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 16, 18)
    pdf.add_page()

    pdf.write_block("VEX Robotics & Base Bot Quiz", size=18, style="B", lh=9)
    pdf.write_block("OCN NI Level 2 IT | Presentation #141", size=11, color=(60, 60, 60), lh=6)
    pdf.write_block(
        "Topic: Build, drive, program and diagnose a VEX Base Bot",
        size=11,
        color=(60, 60, 60),
        lh=6,
    )
    pdf.ln(2)
    pdf.write_block(
        "Microsoft Forms Quick Import tip: upload this PDF, choose Quiz, then review. "
        "Questions are numbered. Options use A. B. C. D. Each choice question ends with "
        "Answer: X so Forms can mark the correct option. Confirm points and feedback after import.",
        size=10,
        style="I",
        color=(80, 80, 80),
        lh=5,
    )
    pdf.ln(3)
    y = pdf.get_y()
    pdf.set_draw_color(0, 189, 165)
    pdf.set_line_width(0.7)
    pdf.line(pdf.l_margin, y, pdf.l_margin + pdf.epw, y)
    pdf.ln(5)

    for i, (q, opts, ans, _why) in enumerate(QUESTIONS, start=1):
        if pdf.get_y() > 250:
            pdf.add_page()
        pdf.write_block(f"{i}. {q}", size=12, style="B", lh=6)
        pdf.ln(1)
        for li, opt in enumerate(opts):
            pdf.write_block(f"{LETTERS[li]}. {opt}", size=11, lh=6)
        pdf.ln(1)
        pdf.write_block(f"Answer: {ans}", size=11, style="B", color=(0, 133, 116), lh=6)
        pdf.write_block("Points: 1", size=10, color=(90, 90, 90), lh=5)
        pdf.ln(3)

    pdf.write_block("Short answer", size=14, style="B", lh=7)
    pdf.ln(2)
    start = len(QUESTIONS) + 1
    for j, q in enumerate(OPEN, start=start):
        if pdf.get_y() > 250:
            pdf.add_page()
        pdf.write_block(f"{j}. {q}", size=12, style="B", lh=6)
        pdf.write_block("Open text", size=10, style="I", color=(90, 90, 90), lh=5)
        pdf.ln(4)

    out = OUT_DIR / "vex-base-bot-forms-quiz.pdf"
    pdf.output(out)
    return out


def build_answer_key() -> Path:
    key = QuizPDF("Teacher key | #141 VEX Base Bot")
    key.alias_nb_pages()
    key.set_auto_page_break(auto=True, margin=18)
    key.set_margins(18, 16, 18)
    key.add_page()
    key.write_block("VEX Base Bot Quiz - Teacher answer key", size=16, style="B", lh=8)
    key.write_block(
        "After Microsoft Forms Quick Import, open each question, confirm the correct option, "
        "set 1 point, and paste the feedback line below.",
        size=10,
        style="I",
        color=(80, 80, 80),
        lh=5,
    )
    key.ln(4)
    for i, (q, opts, ans, why) in enumerate(QUESTIONS, start=1):
        correct = opts[LETTERS.index(ans)]
        key.write_block(f"{i}. Answer {ans} - {correct}", size=11, style="B", lh=5)
        key.write_block(why, size=10, color=(70, 70, 70), lh=5)
        key.ln(2)
    key.write_block(
        "13. Sample: loose cables make good code fail; check wiring before rewriting loops.",
        size=11,
        style="B",
        lh=5,
    )
    key.ln(2)
    key.write_block(
        "14. Sample: rotation/encoder = turns; distance = range; bumper = contact; IMU = heading.",
        size=11,
        style="B",
        lh=5,
    )
    out = OUT_DIR / "vex-base-bot-forms-quiz-answer-key.pdf"
    key.output(out)
    return out


if __name__ == "__main__":
    quiz = build_forms_quiz()
    key = build_answer_key()
    print(f"wrote {quiz} ({quiz.stat().st_size} bytes)")
    print(f"wrote {key} ({key.stat().st_size} bytes)")
