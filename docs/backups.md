# 💾 Manual Backups & Data Archiving

Because StarNote currently stores all data locally on your device, your notes are vulnerable if your device is lost, damaged, or the app is uninstalled. This guide covers the manual "fail-safe" methods to ensure your notes are never lost.

---

## 🛠️ The Manual Export Method (.starnote)

The `.starnote` file is the app's native format. It preserves all vector data, layers, and "Smart Table" properties. Use this for full notebook backups.

### **Step-by-Step Export**

1.  **Select your Notebook**
    In the main Library view, long-press on the notebook cover you wish to back up.
2.  **Choose Export**
    Tap the **Export** icon (usually a box with an upward arrow) and select **StarNote Format (.starnote)**.
3.  **Choose Destination**
    Save the file to your device's internal "Files" app, or better yet, a physical USB-C drive or external SSD.

!!! info "Best Practice"
    At the end of every quarter, we recommend exporting your entire module folder as a single `.starnote` archive.

---

## 📄 Exporting Notes

!!! danger "PDFs are Non-Editable"
    Once exported as a PDF, you cannot "re-import" the handwriting into StarNote as editable vectors.

* **Editable PDF:** Best if you plan to annotate further in a different PDF reader.
* **Non Editable PDF:** After being exported, cannot be further edited in other PDF applications, making it more suitable for file preservation.
* **Picture:** Single exported image can be viewed directly, whereas for multiple selections, it must be unzipped before viewing.
* **StarNote:** Full note contents retained in `.starnote` file format, backup or sharing supported.

---

## 🚨 Troubleshooting Corrupt Backups

If a backup fails to import, it is usually due to one of the following:

| Issue | Solution |
| :--- | :--- |
| **Insufficient Storage** | Ensure your tablet has at least 2GB of free space before attempting a large export. |
| **File Extension Error** | Ensure the file ends in `.starnote`. Do not manually rename the file extension. |
| **Version Mismatch** | A backup created in v1.3.4 may not open in v1.2.0. Always keep the app updated. |

---

### **Need to link to the Cloud?**
If you prefer an automated approach over manual files, head over to the **[Cloud Backup Guide](sync.md)** to set up Google Drive or OneDrive integration.
