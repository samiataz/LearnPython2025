from midiutil import MIDIFile
import random

midi = MIDIFile(6)  # 6 tracks: drums, bass, piano, horns, guitar, solo
tempo = 180
duration_seconds = 180
beats_per_minute = tempo
beats_total = int((duration_seconds / 60) * beats_per_minute)

for track in range(6):
    midi.addTempo(track, 0, tempo)

# Drums (channel 9 - track 0)
for i in range(beats_total):
    beat = i * 0.5
    midi.addNote(0, 9, 36, beat, 0.25, 100)  # Kick
    midi.addNote(0, 9, 42, beat + 0.25, 0.25, 80)  # Hi-hat
    if i % 4 == 2:
        midi.addNote(0, 9, 38, beat, 0.25, 90)  # Snare

# Walking Bass (track 1, channel 1)
bass_notes = [36, 38, 40, 41, 43, 45, 47, 48]
for i in range(beats_total):
    note = random.choice(bass_notes)
    midi.addNote(1, 1, note, i * 0.5, 0.5, 90)

# Piano Comping (track 2, channel 2)
chords = [(60, 64, 67), (62, 65, 69), (59, 63, 67), (60, 64, 69)]
for i in range(beats_total // 4):
    beat = i * 2
    chord = random.choice(chords)
    for note in chord:
        midi.addNote(2, 2, note, beat, 1.5, 70)

# Horns Melody & Solo (track 3, channel 3)
melody_notes = [72, 74, 76, 77, 79, 81, 83, 84]
for i in range(beats_total):
    if i % 8 < 4:  # alternating melody / solo sections
        note = random.choice(melody_notes)
        midi.addNote(3, 3, note, i * 0.5, 0.5, 100)

# Guitar Comping + Solo (track 4, channel 4)
guitar_chords = [(52, 55, 59), (50, 53, 57), (55, 59, 62)]
for i in range(beats_total // 4):
    beat = i * 2
    chord = random.choice(guitar_chords)
    for note in chord:
        midi.addNote(4, 4, note, beat, 1.5, 85)

# Guitar Solo Lines (track 5, channel 4, later section)
for i in range(beats_total // 3, beats_total):
    note = random.choice([64, 67, 69, 71, 72, 74, 76, 79])
    midi.addNote(5, 4, note, i * 0.5, 0.5, 110)

# Save the file
file_path = "orchestral_jazz_3min_with_solos.mid"
with open(file_path, "wb") as f:
    midi.writeFile(f)

print(f"MIDI file created: {file_path}")