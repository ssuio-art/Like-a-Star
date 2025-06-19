# Interactive Audio Visualizer with p5.js

![Preview](preview.png)

This is an interactive audio visualizer project created with p5.js. The project combines beautiful visual effects with audio playback to create a dynamic "Like A Star" themed experience. This project serves as a learning exercise for p5.js and is developed using the Cursor editor.

## Development Environment

- **Editor**: [Cursor](https://cursor.sh/) - A modern AI-powered code editor
- **Version Control**: Git for version control
- **Development Tools**: Chrome DevTools for debugging and performance optimization

## Features

### 🎵 Audio Player
- **Audio Playback**: Full-featured audio player with play/pause controls
- **Progress Bar**: Interactive progress bar with drag-to-seek functionality
- **Volume Control**: Adjustable volume slider with real-time feedback
- **Time Display**: Current time and total duration display
- **Audio File**: Uses `audio.wav` file for playback

### ⭐ Starry Sky Visual Effects
- **Dynamic Star System**: 300 stars rotating around the bottom-right corner
- **Smooth Rotation**: Clockwise rotation animation with varying speeds
- **Audio-Reactive Stars**: Stars twinkle and change brightness based on audio intensity
- **Twinkling System**: Stars respond to audio with natural twinkling effects
- **Full Canvas Coverage**: Stars distributed across the entire canvas

### 🌟 Shooting Stars
- **Audio-Triggered**: Shooting stars appear based on audio intensity
- **Dynamic Effects**: Shooting stars with varying speeds and trails
- **Visual Enhancement**: Adds dynamic movement to the starry sky

### 📊 Audio Visualization
- **FFT Analysis**: Real-time frequency analysis of audio
- **Volume Meter**: Visual volume meter showing audio levels
- **Audio Integration**: Seamless integration between audio playback and visual effects

## Tech Stack

- **p5.js** - For creating interactive visual effects and audio processing
- **p5.sound** - For audio playback and FFT analysis
- **HTML5 Audio API** - For audio file handling
- **CSS3** - For modern UI styling and animations
- **JavaScript** - For interactive functionality

## How to Run

1. Ensure your browser supports Web Audio API
2. Place an `audio.wav` file in the project directory
3. Open `index.html` file in a web browser
4. Use the audio controls to play music and watch the visual effects!

## Audio Controls

### Playback Controls
- **Play/Pause Button**: Control audio playback
- **Progress Bar**: 
  - Click to jump to specific position
  - Drag to seek through the audio
  - Real-time progress display
- **Volume Slider**: Adjust audio volume (0-100%)
- **Time Display**: Shows current time and total duration

### Visual Interaction
- Stars automatically respond to audio intensity
- Higher audio levels create more twinkling effects
- Shooting stars appear during loud passages
- Volume meter provides real-time audio feedback

## Project Structure

```
p5-lab/
├── index.html          # Main HTML file with audio controls
├── audio.wav           # Audio file for playback
├── style.css           # CSS styling for the interface
├── server.py           # Local development server
├── preview.png         # Project preview image
└── README.md           # This file
```

## Development Notes

This project demonstrates how to:
- Create dynamic visual effects using p5.js
- Integrate audio playback with visual feedback
- Implement interactive audio controls
- Create smooth animation effects
- Build responsive audio visualizers
- Use modern CSS for UI design
- Handle audio file loading and playback

## Key Features Implementation

### Audio System
- Uses p5.sound library for audio playback
- FFT analysis for real-time audio visualization
- Custom audio controls with modern UI

### Visual System
- 300 dynamically positioned stars
- Audio-reactive twinkling effects
- Shooting star system
- Smooth rotation animations

### UI/UX
- Modern, starry-night themed design
- Responsive audio controls
- Real-time feedback and displays
- Intuitive drag-and-seek functionality

## Future Enhancements

- [ ] Add multiple audio file support
- [ ] Implement audio effects and filters
- [ ] Add more visual effect variations
- [ ] Create preset visual themes
- [ ] Add keyboard shortcuts for controls

## License

MIT License 