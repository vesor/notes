# Install ubuntu 16.04:
just format a udisk to fat32
and copy all files from the ubuntu install iso
then boot from udisk

(Bios hotkey: F9 to show boot list, F10 to go bios settings.)

ACPI error:
Seems ubutun 16.04 doesn't support the ACPI on this motherboard,
so must add "acpi=off" option when boot linux.
See: https://askubuntu.com/questions/160036/how-do-i-disable-acpi-when-booting

(acpi_rev_override=5 not working)
(Without ACPI, the suspend not working. Reboot works. 
Shutdown cannot cutoff power automatically, you need manually press power button after shutdown.)
