# Pelagica Themes

## Creating a Custom Pelagica Theme

Pelagica themes are defined as JSON files following the structure below:

```json
{
    "name": "Verdant",
    "author": "KartoffelChipss",
    "description": "Verdant is a fresh, modern green-inspired theme that blends soft botanical tones with clean neutrals to create a calm, natural interface.",
    "version": "1.0",
    "colors": {
        "light": {
            "accent": "oklch(0.95 0.03 145)",
            "accent-foreground": "oklch(0.25 0 0)",
            "background": "oklch(0.99 0 0)",
            "border": "oklch(0.90 0 0)",
            "brand": "oklch(0.72 0.20 150)",
            "card": "oklch(1 0 0)",
            "card-foreground": "oklch(0.17 0 0)",
            "chart-1": "oklch(0.72 0.20 150)",
            "chart-2": "oklch(0.68 0.18 130)",
            "chart-3": "oklch(0.62 0.16 170)",
            "chart-4": "oklch(0.78 0.14 120)",
            "chart-5": "oklch(0.74 0.17 160)",
            "destructive": "oklch(0.62 0.24 25)",
            "foreground": "oklch(0.17 0 0)",
            "input": "oklch(0.92 0 0)",
            "muted": "oklch(0.95 0 0)",
            "muted-foreground": "oklch(0.55 0 0)",
            "popover": "oklch(1 0 0)",
            "popover-foreground": "oklch(0.17 0 0)",
            "primary": "oklch(0.72 0.16 150)",
            "primary-foreground": "oklch(0.99 0 0)",
            "ring": "oklch(0.72 0.20 150)",
            "secondary": "oklch(0.96 0.03 145)",
            "secondary-foreground": "oklch(0.25 0 0)",
            "sidebar": "oklch(0.97 0 0)",
            "sidebar-accent": "oklch(0.94 0.04 145)",
            "sidebar-accent-foreground": "oklch(0.25 0 0)",
            "sidebar-border": "oklch(0.90 0 0)",
            "sidebar-foreground": "oklch(0.17 0 0)",
            "sidebar-primary": "oklch(0.72 0.20 150)",
            "sidebar-primary-foreground": "oklch(0.99 0 0)",
            "sidebar-ring": "oklch(0.72 0.20 150)"
        },
        "dark": {
            "accent": "oklch(0.22 0.02 150)",
            "accent-foreground": "oklch(0.98 0 0)",
            "background": "oklch(0.12 0.02 150)",
            "border": "oklch(1 0 0 / 10%)",
            "card": "oklch(0.16 0.02 150)",
            "card-foreground": "oklch(0.96 0 0)",
            "chart-1": "oklch(0.78 0.26 150)",
            "chart-2": "oklch(0.74 0.22 130)",
            "chart-3": "oklch(0.82 0.20 170)",
            "chart-4": "oklch(0.70 0.24 120)",
            "chart-5": "oklch(0.76 0.23 160)",
            "destructive": "oklch(0.70 0.25 25)",
            "foreground": "oklch(0.96 0 0)",
            "input": "oklch(1 0 0 / 15%)",
            "muted": "oklch(0.22 0.02 150)",
            "muted-foreground": "oklch(0.70 0 0)",
            "popover": "oklch(0.16 0.02 150)",
            "popover-foreground": "oklch(0.96 0 0)",
            "primary": "oklch(0.76 0.18 150)",
            "primary-foreground": "oklch(0.15 0 0)",
            "ring": "oklch(0.78 0.26 150)",
            "secondary": "oklch(0.24 0.02 150)",
            "secondary-foreground": "oklch(0.96 0 0)",
            "sidebar": "oklch(0.16 0.02 150)",
            "sidebar-accent": "oklch(0.28 0.05 150)",
            "sidebar-accent-foreground": "oklch(0.96 0 0)",
            "sidebar-border": "oklch(1 0 0 / 10%)",
            "sidebar-foreground": "oklch(0.96 0 0)",
            "sidebar-primary": "oklch(0.78 0.26 150)",
            "sidebar-primary-foreground": "oklch(0.15 0 0)",
            "sidebar-ring": "oklch(0.78 0.26 150)"
        }
    },
    "radius": "0.75rem",
    "modes": ["light", "dark"]
}
```

Each theme must include:

- **name** – The display name of your theme
- **author** – Your name or username
- **description** – A short summary of the theme
- **version** – Theme version (e.g. `1.0`)
- **colors** – Separate color definitions for `light` and/or `dark` mode
- **radius** – Border radius used by the theme
- **modes** – Supported modes (`light`, `dark`, or both)

Make sure all required color tokens are provided for each supported mode to ensure full compatibility.

---

## Using a Custom Theme

To install your custom theme on your server:

1. Go to **Pelagica Settings** (Requires an administrator account).
2. Navigate to the **Themes** tab.
3. Click **Upload New Theme**.
4. Select your JSON file.

After uploading, you can:

- Set it as the **server default theme**, applying it to all users.
- Use it only for yourself via **Preferences → Theme**.

---

## Installing a Theme from the Repository

To install a theme directly from the repository:

1. Open **Pelagica Settings** (Requires an administrator account).
2. Go to the **Themes** tab.
3. Click **Browse Themes**.
4. Click **Install** on your desired theme.

Once installed, you can activate it the same way as a custom theme.

---

## Publishing Your Theme to the Repository

You can share your theme with others by adding it to the official repository.

### Option 1 - Open an Issue (Simplest)

- Create a new issue.
- Attach your theme JSON file.
- Wait for manual review and addition.

> Note: This process may take some time, as themes are added manually.

### Option 2 - Submit a Pull Request (Recommended)

1. Clone the repository.
2. Add your theme JSON file to the `themes` folder.
3. Add preview images to the `assets` folder.
4. Add your theme entry to the `index.json` file.
5. Generate a new UUIDv4 for your theme ID  
   (You can use https://www.uuidgenerator.net).
6. Open a pull request.

Submitting a pull request ensures faster integration and gives you full control over how your theme is presented.
