# ☁️ Cloud Backup & Data Safety

Ensuring your notes are backed up is critical for any user. While **Real-Time Live Syncing** (device-to-device instant updates) is not yet a feature of StarNote, you can protect your data using the built-in **Cloud Backup** system.

!!! warning "Live Sync vs. Cloud Backup"
    StarNote does **not** currently support live syncing. If you edit a note on your device, it will not automatically appear on your other devices in real-time. You must manually "Restore" from a backup to move data between devices.

---

## 🛠️ Setting Up Automated Backups

StarNote allows you to link your favorite cloud provider to store snapshots of your `.starnote` library.

=== "Google Drive"

    1.  Open StarNote and tap the **Settings** (gear icon) in the top-left.
    2.  Navigate to **Cloud backup**
    3.  Select bind **Google Drive** and sign in with your student or personal account.
    4.  Toggle **Auto-Backup** to `ON`. 
    
    !!! tip "Storage Tip"
        Since StarNote uses vector data, backups are typically very small (usually under 5MB per notebook). Even a free Google Drive account could last you through your entire degree.

=== "OneDrive"

    1.  Open StarNote and tap the **Settings** (gear icon) in the top-left.
    2.  Navigate to **Cloud backup**
    3.  Select bind **OneDrive** and sign in with your student or personal account.
    4.  Toggle **Auto-Backup** to `ON`.

    !!! tip "Storage Tip"
        Since StarNote uses vector data, backups are typically very small (usually under 5MB per notebook). Even a free OneDrive account could last you through your entire degree.

---

## 📂 Moving Data Between Devices

If you are switching from one device to another, follow this "Snapshot" method:

1.  **On the Original Device:** Go to Cloud Backup and tap **Upload Backup**.
2.  **On the New Device:** Sign in to the *same* cloud provider and account.
3.  **Restore:** Tap **Download & Restore**.
 
    !!! warning "Warning"
        This will create **duplicates** any existing notes on the new device in addition to the versions from the cloud. If you want to avoid duplicates and you know what you are doing, you can select and delete all of your notes before restoring a backup to simply have a single copy of the backed up notes. **Note that any changes that are not backed up will be lost in this way!** Backups cannot be merged. If you want to keep a note that's not in the backup being restored, simply do not delete it.

---

## 💾 Local Backups

If you prefer not to use the cloud, or if you want to archive a specific module's notes at the end of the semester, use the **Local Export** feature.

=== "Local Backup"

    1.  Open StarNote and tap the **Settings** (gear icon) in the top-left.
    2.  Navigate to **Local backup**
    3.  Tap "Backup now"
    4.  Optionally toggle **Auto-Backup** to `ON`. 
    
=== "Importing a Backup"

    1.  Open StarNote and tap the **Settings** (gear icon) in the top-left.
    2.  Navigate to **Local backup**
    3.  Tap "Import" and select the backup file you would like to import.

---

## ❓ FAQ: Data & Sync

### **Can I sync my notes to my Windows PC?**
Not yet. Because there is no native Windows app, you can only view your notes on PC by exporting them as **PDFs** and uploading them to your cloud drive or transferring them manually.

### **Can I sync my notes to my other devices?**
StarNote does **not** currently support live syncing. If you edit a note on your device, it will not automatically appear on your other devices in real-time. You must manually "Restore" from a backup to move data between devices. While **Real-Time Live Syncing** (device-to-device instant updates) is not yet a feature of StarNote, you can manually transfer your data using the built-in **Cloud Backup** system.

### **How often should I backup?**
The more often the better. We recommend using the **Auto-Backup** setting.

### **What happens if I delete the app?**
If you haven't set up a Cloud Backup or exported your files manually, **your notes will be permanently lost**. Always ensure your backup screen stays open until the status says "Success" before offloading the app.
