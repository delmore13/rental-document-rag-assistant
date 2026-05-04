from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_sample_lease_pdf(output_path: str = "data/sample_lease.pdf") -> None:
    Path("data").mkdir(exist_ok=True)

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    lines = [
        "Sample Residential Lease Agreement",
        "",
        "1. Rent Payment",
        "The tenant is responsible for paying rent on the first day of each month.",
        "Late fees may apply if rent is not received by the fifth day of the month.",
        "",
        "2. Pet Policy",
        "Pets are not allowed unless approved in writing by the landlord.",
        "If approved, the tenant may be required to pay an additional pet deposit.",
        "",
        "3. Security Deposit",
        "The security deposit will be returned within 45 days after move-out,",
        "minus any lawful deductions for unpaid rent, damages, or cleaning costs.",
        "",
        "4. Maintenance",
        "The tenant must keep the property clean and report maintenance issues promptly.",
        "The landlord is responsible for major repairs unless damage was caused by the tenant.",
    ]

    y = height - 72

    for line in lines:
        c.drawString(72, y, line)
        y -= 18

    c.save()


if __name__ == "__main__":
    create_sample_lease_pdf()
    print("Created data/sample_lease.pdf")