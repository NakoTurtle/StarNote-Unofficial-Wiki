document.addEventListener("DOMContentLoaded", function() {
  // Configuration
  const DARK_THEME_NAME = "slate"; // The name of your dark palette in mkdocs.yml
  const LIGHT_COLOR = "#333333";   // Text color for Light Mode
  const DARK_COLOR = "#eef2f3";    // Text color for Dark Mode

  // Function to update colors
  const updateMarkmap = () => {
    const currentScheme = document.body.getAttribute("data-md-color-scheme");
    const isDark = currentScheme === DARK_THEME_NAME;
    const targetColor = isDark ? DARK_COLOR : LIGHT_COLOR;

    // Target all Markmap text elements
    document.querySelectorAll(".markmap svg text").forEach(el => {
      el.style.fill = targetColor;
    });
    
    // Optional: Target lines (paths) if they are hard to see
    document.querySelectorAll(".markmap svg path").forEach(el => {
      // Only change stroke if it's not a specific colored branch
      // Remove this check if you want ALL lines to be the theme color
      if (!el.getAttribute("stroke") || el.getAttribute("stroke") === "black") {
         el.style.stroke = targetColor;
      }
    });
  };

  // 1. Watch for theme changes
  const observer = new MutationObserver(updateMarkmap);
  observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });

  // 2. Also run once on initial load
  // We use a slight delay to ensure Markmap has finished rendering the SVG
  setTimeout(updateMarkmap, 500);
});
