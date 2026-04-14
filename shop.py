import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def clear_screen():
    os.system('clear')

def show_signature():
    sig = "[bold cyan]DEVELOPED BY: VIBE CODER (LAGOS)[/bold cyan]"
    console.print(Panel.fit(sig, border_style="blue"))

def show_menu():
    clear_screen()
    show_signature()
    console.print(Panel("[bold white]LQC SMART SHOP MANAGER v4.2[/bold white]", subtitle="Case-Insensitive Search Active", border_style="magenta"))
    console.print("[1] 🔍 Search Model/Combo")
    console.print("[2] ➕ Add New Model")
    console.print("[3] 📜 View All Records")
    console.print("[Q] Exit App")

def search_model():
    query = input("\nSearch Name or Model: ").strip().lower()
    table = Table(title=f"Results for '{query}'", show_lines=True)
    table.add_column("Compatibility List", style="green")
    
    found = False
    try:
        with open("database.txt", "r") as f:
            for line in f:
                if query in line.lower() and not line.startswith("#"):
                    table.add_row(line.strip())
                    found = True
    except FileNotFoundError:
        console.print("[bold red]Error: database.txt not found![/bold red]")
        return
    
    if found: console.print(table)
    else: console.print(f"[bold red]'{query}' Not Found.[/bold red]")
    input("\nPress Enter...")

def add_model():
    name = input("Enter Phone Name (e.g. Spark 20): ").title()
    model = input("Enter Model No (e.g. KJ5): ").upper()
    combo = input("Enter what else it fits (optional): ")
    with open("database.txt", "a") as f:
        f.write(f"\n{name} ({model}) / {combo}")
    console.print("[bold green]Success! Database Updated.[/bold green]")
    input("\nPress Enter...")

def view_all():
    table = Table(title="All Shop Records", show_lines=True)
    table.add_column("Stored Combos", style="yellow")
    try:
        with open("database.txt", "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    table.add_row(line.strip())
        console.print(table)
    except FileNotFoundError:
        console.print("[bold red]Database is empty.[/bold red]")
    input("\nPress Enter...")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("\nAction: ").lower()
        if choice == '1': search_model()
        elif choice == '2': add_model()
        elif choice == '3': view_all()
        elif choice == 'q': break
