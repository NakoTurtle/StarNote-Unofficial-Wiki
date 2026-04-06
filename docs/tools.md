!!! warning "Important"
    This wiki was not made by the developers of StarNote and may not be completely accurate!
    
# Tools

This guide covers the technical specifications and customization options for pens.

---
!!! question "Remember"
    Some of these features will only work properly when using an active stylus.
    
##  Core Pen Types
StarNote uses a "Pen Box" system allowing for **16 custom presets**. Tap any tool in the toolbar twice to access its specific configuration menu.

### 1. Fountain Pen
* **Behavior:** A reliable pen that works well for writing naturally.
* **Dynamics:** Always has some level of pressure sensitivity, even when set to 0%.
* **Settings:** 
    * Pressure Sensitivity
    * Thickness
    * Stroke Stabilization

### 2. Calligraphy Pen
* **Behavior:** A fancy pen that works well for making beautiful headings or labels.
* **Dynamics:** Makes thicker lines on downwards strokes and thinner lines on upwards strokes.
* **Settings:** 
    * Thickness
    * Stroke Stabilization

### 3. SoftPaint Brush (v1.2+)
* **Behavior:** A flowy pen that that's great for sketching or making headings.
* **Dynamics:** Fills the stroke as you write and tapers the end based on the writing speed.
* **Settings:** 
    * Thickness

### 4. Ballpoint Pen
* **Behavior:** A consistent pen great for making precise diagrams or neat handwriting and drawing.
* **Dynamics:** Uniform line width regardless of pressure or speed.
* **Settings:** 
    * Thickness
    * Stroke Stabilization

### 5. Pencil
* **Behavior:** A semi transparent pen great for coloring, shading or making quick sketches.
* **Dynamics:** Appends brushes to existing strokes, making them darker until saturated.
* **Settings:**  
    * Pressure Senstivity
    * Thickness
    * Density

### Pen Settings
Customize how the strokes react to your stylus to match your writing style.

* **Pressure Sensitivity** - Makes the pen stroke thickness (and density in the case of the pencil) react to the writing pressure measured by your tablet's stylus. Force-thickness curves are not fully customizable however.
* **Thickness** - Adjust the thickness of the stroke in millimeters.
* **Stroke Stabilization** - Reduces "jitters" caused by writing and enables neater handwriting and better curved strokes.
* **Density** - Changes the hardness level of the pencil so it writes darker or lighter.
* **One-Stroke Shaping** - If you hold the stylus at the end of a stroke, the app snaps the line into a perfect version of the shape drawn. See the shapes tool for more info on supported shapes for this tool.
 
---

##  Utility Writing Tools
Tools designed for interaction and correction.

### Highlighter:
* **Behavior:** Semi-transparent ink.
* **Dynamics:** Layers *behind* existing handwriting to prevent obscuring notes.
#### Other Highlighter Options:
* **Draw Straght Line:** Automatically snaps your highlight to a straight line.
### Eraser:
A tool to precisely remove anything you want.
#### Eraser Modes:
* **Stroke Eraser:** Deletes the entire continuous line/shape.
* **Partial Eraser:** Deletes only the pixels the eraser touches (standard eraser).
* **Circular selection eraser:** Deletes everything within a region you circle around.
#### Other Eraser Options:
* **Size:** Changes the size of the eraser brush.
* **Scribble to Erase:** Enables erasing content by simply scribbling it out. (1)
    { .annotate }
    
    1.  Only available on android.

* **Erase Highlighter Only:** Makes so the eraser tool only removes highlighter without disturbing other elements.
* **Erase Tape Only:** Makes so the eraser tool only removes tape without disturbing other elements.
* **Select Stroke:** 
* **Auto-Deselect Eraser:** When enabled, the app automatically returns back to the tool you used before, once you lift the stylus after erasing.
### Lasso:
Tool for selecting objects in your notes in order to move or edit them.
#### Lasso Modes:
*  **Free Lasso:** Makes so you can draw a shape exactly around what you want to select.
*  **Rectangular Lasso:** Makes use of a rectangular selection box.
#### Other Lasso Options (Include or Exclude):
* Shape
* Picture/Sticker
* Tape
* Text box
* Handwriting
* Highlighter
* Link
* Tag
* Table
### Picture Tool:
Allows the user to insert images directly into their notes.
#### Picture Tool Options:
* **Insert From Album:** Allows the user to insert an image from the device gallery.
* **Take Photo:** Opens the camera to take a picture to insert.
### Textbox:
Allows the user to insert typed text directly into their notes.
#### Textbox Options:
* **Font Type:** Changes the face of the font.
* **Font Size:** Changes the width and height of the font.
* **Multiply:** Unknown
* **Font Styles:** 
    * Bold
    * Italics
    * Underline
* **Alignment:**
    * Left
    * Center
    * Right
* **Font Color:** Features a set of 5 preset, but customizable colors.
### Excerpt Pen:
This is a tool for "citing" parts of your notes either within the same note, or to another note, allowing you to jump back to the original note. (Jumping not available when placing the excerpt in the same note)
#### Excerpt Pen Modes:
* **Text Excerpt:** Allows exceprting typed text in your notes.
* **Box Excerpt:** Allows excerpting any part of your notes.
#### Excerpt Pen Options:
* **Show the excerpt icon:** Enables or disables the icon on excerpts.
### Tagging Tool:
Allows the user to add new or existing tags to their notes. These tags are resizable and can be filtered by in the home screen side bar.
### Shape Tool:
Allows the user to add specialized shapes to their notes.
#### List of the Available Shapes:
* Straight Line
* Straight Wave Line
* Arc
* Straight Dashed line
* Straight Arrow
* Straight Double Sided Arrow
* Curved Arrow
* Curved Double Sided Arrow
* Angled Lines
* 2D Axes
* 3D Axes
* 2D Axes with 45º arrow
* Curly Bracket
* Scalene Triangle
* Isoceles Traingle
* Equilateral Triangle
* Right Triangle
* Square
* Rectangle
* Rounded Rectangle
* Pill Shape
* Scalene Trapezoid
* Isoceles Trapezoid
* Right Trapezoid
* Rhomboid
* Diamond
* Rhombus
* Pentagon
* Hexagon
* Octagon
* Circle
* Ellipse
* Star
* Cone
* Triangular Pyramid
* Square Pyramid
* Various Triangular Prisms
* Rectangular Prism
* Cube
* Pentagonal Prism
* Hexagonal Prism
* Cylinder
* Tube
* Truncated Rectangular Pyramid
* Truncated Cone
* Ellipsoid
* Sphere
* Half Sphere
#### Shape Tool Options:
* **Stroke Thickness:** Changes the width of the lines used for drawing the shapes.
* **Shape Fill:** Allows for a color to be selected as the fill color of the shape. Can also be synced with the stroke color of the shape, with a specified opacity.
### Sticker:
* Allows users to place one of the preexisting or custom added stickers to their notes, primarily for decoration.
### The Tape Tool:
Creates opaque, removable strips. Tap to "reveal" what is underneath.
* *Usage:* Perfect for **Active Recall**—hide formulas or answers while studying.
#### Tape Tool Modes:
 * **Draw Straight Line:** Makes the tape tool only draw in straight lines.
 * **Rectangle Drawing:** Makes the tape tool able to draw rectangular shapes at custom sizes.
#### Tape Tool Options:
* **Show All Tapes:** Toggle to show or hide all tapes in the note.
* **Style:** Changes the pattern displayed on the tape surface.
* **Thickness:** Changes the width of the tape for the straight tape mode.
* **Clear tape on current page:** Removes all tape drawn on the current page of the note.
* **Clear tapes on all pages:** Removes all tape drawn anywhere in the current note.
### The Laser Pointer: 
A temporary ink tool for "drawing" attention to parts of a diagram during a presentation or review session. The ink disappears after a few seconds.
#### Laser Pointer Modes:
* **Line:** Leaves a trail when moving the laser pointer.
* **Dot:** Only shows the laser pointer dot.
#### Other Laser Pointer Options:
* **Thickness:** Changes the size of the pointer.
* **Duration:** Changes the length of time the laser stays before fading away.   
### Ruler:
Toggle to show a ruler on the screen that you can move or rotate using two fingers. The measurement units are not specified, but angle is in degrees. When drawing towards or against the ruler, the line snaps against the straight edge and stays there until the end of the stroke.
### Magnifier:
Tap to show a magnified view of the zoom box. 
#### Magnifier Usage:
* The zoom box is resizable, but the magnified view is not. 
* The magnifier is designed particularly for writing purposes, and the arrow buttons are designed to help with it. Simply hit the left or right arrow buttons to move the zoom box in that direction. Hit the "enter" arrow to move the box downwards to the next line and back to the left of the page. When auto-advance is toggled on, the zoom box moves automatically when your stroke crosses the resizable edge area on the right.
* To close the magnifier, hit the cross on the magnified view.
### Table:
The table tool allows users to insert tables into their notes.
#### Table Tool Modes:
* **Header Row:** Toggles whether the drawn table has a header row or not.
* **Header Column:** Toggles whether the drawn table has a header column or not.
* **Rows:** Changes the number of rows in the drawn table. (1-50)
* **Columns:** Changes the number of columns in the drawn table. (1-50)
* **Border Thickness:** Changes the thickness of the table borders.
* **Fill Color:** Toggles whether the table cells have a fill color and gives options to change the color when enabled.
### Toolbar Settings
*  
### Colors:
*  
### Brush Toolbar:
*  
---

##  Color & Aesthetic Control
* **Hex Code Support:** Input specific 6-digit codes for exact color matching.
* **Color Dropper:** Select any color from an imported PDF, image, or screenshot to add to your custom palette.
* **Transparency Slider:** Adjust the "Alpha" channel for any pen type to create custom layered effects.

***
