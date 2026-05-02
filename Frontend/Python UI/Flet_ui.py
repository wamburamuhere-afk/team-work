#!/usr/bin/env python3

import flet as ft

def main(page: ft.Page):
    page.title = "Simple Flet App"
    page.window_width = 500
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    
    # ===== State Variables =====
    counter = 0
    
    # ===== Update Functions =====
    def increment_counter(e):
        nonlocal counter
        counter += 1
        counter_text.value = f"Counter: {counter}"
        page.update()
    
    def decrement_counter(e):
        nonlocal counter
        counter -= 1
        counter_text.value = f"Counter: {counter}"
        page.update()
    
    def reset_counter(e):
        nonlocal counter
        counter = 0
        counter_text.value = f"Counter: {counter}"
        page.update()
    
    def on_text_change(e):
        output_text.value = f"You typed: {text_input.value}"
        page.update()
    
    def on_button_click(e):
        if text_input.value.strip():
            output_text.value = f"Hello, {text_input.value}! 👋"
        else:
            output_text.value = "Please enter a name first!"
        page.update()
    
    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()
    
    # ===== UI Components =====
    
    # Header
    header = ft.Text(
        "Flet Demo App",
        size=32,
        weight="bold",
        text_align=ft.TextAlign.CENTER
    )
    
    # === Counter Section ===
    counter_text = ft.Text(
        "Counter: 0",
        size=24,
        weight="bold",
        text_align=ft.TextAlign.CENTER
    )
    
    increment_btn = ft.ElevatedButton(
        text="Increment",
        on_click=increment_counter,
        width=150
    )
    
    decrement_btn = ft.ElevatedButton(
        text="Decrement",
        on_click=decrement_counter,
        width=150
    )
    
    reset_btn = ft.OutlinedButton(
        text="Reset",
        on_click=reset_counter,
        width=150
    )
    
    counter_buttons = ft.Row(
        controls=[increment_btn, decrement_btn, reset_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    
    counter_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Counter", size=20, weight="bold"),
                counter_text,
                counter_buttons
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
        margin=10
    )
    
    # === Text Input Section ===
    text_input = ft.TextField(
        label="Enter your name",
        hint_text="Type something...",
        on_change=on_text_change,
        width=300
    )
    
    greet_btn = ft.ElevatedButton(
        text="Greet Me",
        on_click=on_button_click,
        width=300
    )
    
    output_text = ft.Text(
        "Output will appear here",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.LIGHT_BLUE
    )
    
    input_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Text Input Demo", size=20, weight="bold"),
                text_input,
                greet_btn,
                output_text
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
        margin=10
    )
    
    # === Dropdown Section ===
    dropdown = ft.Dropdown(
        label="Select a color",
        value="Red",
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Yellow"),
            ft.dropdown.Option("Purple")
        ],
        width=300
    )
    
    color_display = ft.Container(
        width=300,
        height=100,
        bgcolor=ft.colors.RED,
        border_radius=10
    )
    
    def on_dropdown_change(e):
        color_map = {
            "Red": ft.colors.RED,
            "Green": ft.colors.GREEN,
            "Blue": ft.colors.BLUE,
            "Yellow": ft.colors.YELLOW,
            "Purple": ft.colors.PURPLE
        }
        color_display.bgcolor = color_map.get(dropdown.value, ft.colors.RED)
        page.update()
    
    dropdown.on_change = on_dropdown_change
    
    dropdown_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Dropdown Demo", size=20, weight="bold"),
                dropdown,
                color_display
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
        margin=10
    )
    
    # === Theme Toggle ===
    theme_btn = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        tooltip="Toggle Theme",
        on_click=toggle_theme
    )
    
    theme_section = ft.Row(
        controls=[theme_btn],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    # ===== Main Layout =====
    page.add(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                header,
                theme_section,
                ft.Divider(),
                counter_section,
                input_section,
                dropdown_section,
                ft.SizedBox(height=20)
            ],
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.app(target=main)