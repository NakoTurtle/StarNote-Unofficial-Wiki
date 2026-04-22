# 📤 PDF Exporting & Sharing

Converting your infinite canvas notes into a standard PDF is usually the final step in the StarNote workflow. This page covers how to convert your expansive notes into a format that anyone can view on any device.

---

## 🛠️ The Export Workflow

StarNote treats the PDF export as a "snapshot" of your vector data. 

!!! info "Vector Fidelity"
    Because StarNote uses a vector engine, your exported PDFs will remain crisp and searchable (if you used typed text).

### **Step-by-Step Guide**

1.  **Open the Export Menu**
    Tap the **Export File** icon (square with upward arrow) either in the toolbar or under the three dot menu.
2.  **Choose PDF Type**
    Choose between Editable and Non-Editable (Flattened) PDF Types.
3.  **Choose a File Name**
4.  **Choose whether or not to include the page background**
5.  Choose between **export only** or **export and share**

???+ info "Please Note" 
     StarNote always exports a local copy to your device (storage/documents/starnote/export) for both **export only** and **export and share**.

---

## 📋 PDF Export Options

<div class="grid cards" markdown>

-   :material-file-pdf-box:{ .lg .middle } __Flattened PDF__
    ---
    Merges all layers into a single image. Best for submissions where you don't want your handwriting to be accidentally moved by the recipient.

-   :material-layers-off:{ .lg .middle } __Editable PDF__
    ---
    Preserves layers so that other PDF annotators can see your strokes as separate objects.

</div>

---

## ⚠️ Important Considerations

!!! danger "Handwriting Searchability"
    As of v1.3.4, StarNote does **not** embed OCR (Optical Character Recognition) data into exported PDFs. While your handwriting looks crisp, you cannot "Ctrl+F" your handwritten notes within a PDF viewer yet.

* **File Size:** Large infinite canvases with many high-res image imports can result in PDFs exceeding 50MB.
* **Hyperlinks:** Any internal links created within StarNote are currently **non-functional** in exported PDFs. They will appear as standard text.

---

### **Need to save the original file?**
If you want to move your work to another tablet while keeping it fully editable, visit the **[Manual Backups (.starnote)](backups.md)** page instead.
