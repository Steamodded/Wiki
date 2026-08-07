# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SMODS Documentation"
copyright = "SMODS Team"
author = "SMODS Team"
release = "0.1"
html_favicon = "icon.png"
html_title = "SMODS Documentation"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_lua_ls"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_Sidebar.md"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ["_static"]
html_theme_options = {
    "globaltoc_expand_depth": 2,
    "accent_color": "orange",
    "show_ai_links": False,
    "show_nav_level": 0,
    "foot_socials": [
        {
            "name": "GitHub",
            "url": "https://github.com/Steamodded/smods",
            "icon": "simple-icons:github",
        }
    ],
}
html_logo = "icon.png"
html_context = {
    "source_type": "github",
    "source_user": "Steamodded",
    "source_repo": "smods",
    "source_edit_template": "https://github.com/Steamodded/Wiki/blob/master/{0}",
}

myst_enable_extensions = [
    "alert",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- LUA LS

lua_ls_project_root = "."
lua_ls_backend = "luals"
primary_domain = "lua"
lua_ls_apidoc_format = "md"
# lua_ls_apidoc_roots = {
#     "SMODS.Center": "lsp_docs",
# }
lua_ls_lua_version = "jit"
lua_ls_apidoc_default_options = {
    "undoc-members": "true",
    "protected-members": "true",
    "globals": "true",
}
