!!! warning "Important"
    This wiki was not made by the developers of StarNote and may not be completely accurate!
    
# 🖋️ StarNote Wiki: Pen Engine & Input Deep Dive

This guide covers the technical specifications and customization options for the **Proprietary Ink Engine** in StarNote (v1.3.4).

---

## 🛠️ Core Pen Types
StarNote uses a "Pen Box" system allowing for **16 custom presets**. Double-tap any tool in the toolbar to access its specific configuration menu.

### **1. Fountain Pen**
* **Behavior:** High pressure sensitivity with a "tapered" stroke.
* **Dynamics:** Speed and pressure dictate line thickness (fast strokes = thin lines).
* **Best For:** Handwriting, titles, and personalized signatures.

### **2. Ballpoint Pen**
* **Behavior:** Uniform line width regardless of pressure or speed.
* **Dynamics:** Extremely consistent and predictable.
* **Best For:** **Technical Drawing.** Ideal for circuit diagrams (Electrotechnique) or free-body diagrams (Strength of Materials) where precision is required.

### **3. Highlighter**
* **Behavior:** Semi-transparent ink.
* **Dynamics:** Layers *behind* existing handwriting to prevent obscuring notes.
* **Special Setting:** **"Smart Straighten"**—automatically snaps your highlight to a straight line.

### **4. SoftPaint Brush (v1.2+)**
* **Behavior:** Textured, soft-edge brush with opacity gradients.
* **Dynamics:** Responds to both pressure and **stylus tilt**.
* **Best For:** Shading 3D objects, stress distribution heatmaps, or grain structure sketches in Material Science.

---

## ⚙️ Advanced Pen Settings
Customize how the glass reacts to your stylus to match your writing style.

* **Stabilization (Smoothing):** * Reduces "jitters" caused by writing on a slippery screen.
    * *Pro-Tip:* Set to **15-20%** for engineering notes to keep handwriting legible without causing input lag.
* **One-Stroke Shaping:** * If you hold the stylus at the end of a stroke, the app snaps the line into a perfect geometric shape (Circle, Square, Triangle) or a perfectly straight line.
* **Pressure Sensitivity Curve:** * Manually adjust the "force-to-thickness" ratio. Useful if you have a naturally heavy or light writing hand.
* **Tilt Support:** * Available for SoftPaint and Fountain tools. Simulates the "angle of the nib" for broad or fine detailing.

---

## 🧰 Utility Writing Tools
Tools designed for interaction and correction rather than permanent note-taking.

* **The Laser Pointer:** A temporary ink tool for "drawing" attention to parts of a diagram during a presentation or review session. The ink disappears after a few seconds.
* **The Tape Tool:** Creates opaque, removable strips. Tap to "reveal" what is underneath.
    * *Usage:* Perfect for **Active Recall**—hide formulas or answers while studying for your A1 exams.
* **Smart Eraser Modes:**
    * **Stroke Eraser:** Deletes the entire continuous line/shape.
    * **Partial Eraser:** Deletes only the pixels the eraser touches (standard eraser).
    * **Auto-Switch:** When enabled, the app automatically returns to your last-used pen as soon as you lift the stylus after erasing.

---

## 🎨 Color & Aesthetic Control
* **Hex Code Support:** Input specific 6-digit codes for exact color matching.
* **Color Dropper:** Select any color from an imported PDF, image, or screenshot to add to your custom palette.
* **Transparency Slider:** Adjust the "Alpha" channel for any pen type to create custom layered effects.

***
