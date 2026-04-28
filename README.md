# LYCHEE APP

<img src="./src/assets/lychee-logo.png" alt="Lychee Logo" width="150" height="150">

## Overview

LYCHEE is a React Native mobile application designed to interface with the LYCHEE-USB hardware device for music management, curation, and discovery. The app provides seamless integration between mobile devices and the LYCHEE hardware ecosystem, enabling users to manage their music library, create playlists, and sync content across platforms.

## Tech Stack

- **Framework**: React Native 0.78.1
- **Language**: TypeScript 5.0.4
- **State Management**: React Hooks & Context
- **Audio Processing**: Custom native modules with FFT analysis
- **Bluetooth**: react-native-ble-plx for LYCHEE device communication
- **Audio Playback**: react-native-track-player
- **UI**: Custom trapezoid-themed components
- **Fonts**: Rigid Square, Neue Haas Grotesk Display Pro
- **Platform Integration**: Spotify API, Apple Music (planned)

## Prerequisites

- **Node.js**: >= 18
- **npm** or **yarn**
- **React Native CLI**: Latest version
- **iOS Development**: Xcode 14+ (for iOS testing)
- **Android Development**: Android Studio (for Android testing)
- **CocoaPods**: For iOS dependencies

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lycheeinc/lychee-app.git
   cd lychee-app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Install iOS dependencies:**
   ```bash
   cd ios && pod install && cd ..
   ```

4. **Run the application:**
   - **iOS:**
     ```bash
     npx react-native run-ios
     ```
   - **Android:**
     ```bash
     npx react-native run-android
     ```

## Project Architecture

```
lychee-app/
├── src/
│   ├── assets/              # Images, fonts, icons
│   │   ├── fonts/           # Custom font files
│   │   ├── icons/           # App icons and UI elements
│   │   └── images/          # Static images and logos
│   ├── components/          # Reusable UI components
│   │   ├── icons/           # Icon components
│   │   ├── Player.tsx       # Audio player component
│   │   ├── SongRow.tsx      # Song list item component
│   │   ├── TabNavigation.tsx # Custom tab navigation
│   │   ├── TrapezoidButton.tsx # Custom button component
│   │   └── ...              # Other UI components
│   ├── screens/             # Application screens
│   │   ├── HomeScreen.tsx   # Main app screen
│   │   ├── LoginScreen.tsx  # Authentication screen
│   │   ├── ConnectUSBScreen.tsx # USB device connection
│   │   └── ...              # Other screens
│   ├── services/            # Business logic and API services
│   │   ├── BLEService.ts    # Bluetooth Low Energy communication
│   │   ├── SpotifyService.ts # Spotify API integration
│   │   ├── AuthService.ts   # Authentication logic
│   │   └── ...              # Other services
│   ├── utils/               # Utility functions and helpers
│   │   ├── AudioFileUtils.ts # Audio file processing
│   │   ├── USBDeviceHelper.ts # USB device communication
│   │   ├── TrackPlayerService.js # Audio playback setup
│   │   └── ...              # Other utilities
│   ├── theme/               # Design system and styling
│   │   ├── layout.ts        # Colors, spacing, layout constants
│   │   └── fonts.ts         # Font definitions
│   ├── types/               # TypeScript type definitions
│   ├── hooks/               # Custom React hooks
│   ├── config/              # App configuration
│   └── data/                # Static data and mock data
├── ios/                     # iOS-specific code and configuration
├── android/                 # Android-specific code and configuration
├── firmware/                # LYCHEE device firmware files
└── package.json             # Dependencies and scripts
```

## Key Features

### 🎵 Music Management
- **Library Sync**: Sync music libraries from Spotify and local files
- **Playlist Management**: Create, edit, and organize playlists
- **Song Metadata**: Rich metadata display with album art, BPM, and audio features
- **File Upload**: Support for multiple audio formats (.mp3, .m4a, .aac, .wav, .ogg, .flac)

### 🔊 Audio Processing - IN DEVELOPMENT
- **Waveform Visualization**: In Development: real-time waveform generation and display
- **FFT Analysis**: In Development: Frequency analysis for audio visualization
- **BPM Detection**: In Development: Automatic tempo detection
- **Audio Features**: In Development: Key detection, energy analysis, and more

### 📱 Device Integration
- **LYCHEE-USB**: Bluetooth communication with LYCHEE hardware
- **File Transfer**: Seamless file transfer to/from device
- **Device Settings**: Configure device preferences and settings
- **Firmware Updates**: Over-the-air firmware update capability

### 🎨 Custom UI
- **Trapezoid Design**: Unique geometric design language
- **Custom Components**: Specialized UI components for music apps
- **Responsive Layout**: Optimized for various screen sizes
- **Dark Theme**: Modern dark interface design

## Core Components

### UI Components

#### TrapezoidButton
Custom button component with stacked trapezoid-on-rectangle design matching the app's design language. Features a trapezoid section on top and rectangle section below with text spanning both areas.
```typescript
<TrapezoidButton
  text="Connect USB"
  onPress={handleConnect}
  backgroundColor={COLORS.PINK}
  textColor="#FFFFFF"
  width={205}
/>
```

#### TrapezoidInput
Custom input component with the same stacked trapezoid-on-rectangle design as TrapezoidButton. Provides consistent styling for text input fields throughout the app.
```typescript
<TrapezoidInput
  placeholder="Enter username"
  value={username}
  onChangeText={setUsername}
  backgroundColor="#CCCCCC"
  width={205}
/>
```

#### SongRow
Displays song information with waveform, metadata, and controls.
```typescript
<SongRow
  song={songData}
  onPlay={handlePlay}
  onAddToPlaylist={handleAddToPlaylist}
  showWaveform={true}
/>
```

#### TabNavigation
Custom tab navigation with trapezoid-shaped tabs.
```typescript
<TabNavigation
  activeTab={activeTab}
  onTabChange={setActiveTab}
  tabs={['songs', 'playlists', 'sets']}
/>
```

### Services

#### BLEService
Handles all Bluetooth Low Energy communication with LYCHEE devices.
```typescript
import bleService from './src/services/BLEService';

// Connect to device
await bleService.connectToDevice(deviceId);

// Send file to device
await bleService.sendFileToDevice(filePath);
```

#### SpotifyService
Manages Spotify API integration for music discovery and library sync.
```typescript
import { SpotifyService } from './src/services/SpotifyService';

// Authenticate with Spotify
await SpotifyService.authenticate();

// Get user playlists
const playlists = await SpotifyService.getUserPlaylists();
```

#### AudioFileUtils
Processes audio files for waveform generation and metadata extraction.
```typescript
import { AudioFileUtils } from './src/utils/AudioFileUtils';

// Extract waveform data
const waveformData = await AudioFileUtils.extractWaveform(filePath);

// Get audio metadata
const metadata = await AudioFileUtils.getMetadata(filePath);
```

## Development Guidelines

### Code Style
- **TypeScript**: Use TypeScript for all new code
- **ESLint**: Follow the configured ESLint rules
- **Prettier**: Use Prettier for code formatting
- **Naming**: Use PascalCase for components, camelCase for functions/variables

### Component Development
- **Functional Components**: Use functional components with hooks
- **Props Interface**: Define TypeScript interfaces for all component props
- **Styling**: Use StyleSheet.create() for component styles
- **Reusability**: Create reusable components in the components directory

### State Management
- **Local State**: Use useState for component-level state
- **Complex State**: Use useReducer for complex state logic
- **Global State**: Use Context API for app-wide state (consider Redux if needed)

### Testing
- **Unit Tests**: Write tests for utility functions and services
- **Component Tests**: Test component rendering and interactions
- **Integration Tests**: Test service integrations and API calls

### Performance
- **Memory Management**: Use HermesMemoryManager for memory optimization
- **Image Caching**: Implement proper image caching for album art
- **Audio Processing**: Optimize audio processing for real-time performance

## API Integration

### Spotify Integration
The app integrates with Spotify Web API for music discovery and library management.

**Setup:**
1. Create a Spotify app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Configure redirect URIs for authentication
3. Add client ID to app configuration

**Key Features:**
- User authentication via OAuth 2.0
- Playlist synchronization
- Track search and discovery
- Audio features analysis

### LYCHEE Device Communication
Communication with LYCHEE hardware devices via Bluetooth Low Energy.

**Protocol:**
- Custom BLE protocol for file transfer
- Metadata synchronization
- Device status monitoring
- Firmware update delivery

## Audio Processing

### Waveform Generation
The app generates waveforms for audio visualization using native modules.

**Process:**
1. Audio file is decoded using native audio libraries
2. PCM data is processed to extract amplitude values
3. Data is downsampled for efficient rendering
4. Waveform is cached for future use

**Supported Formats:**
- MP3, M4A, AAC (lossy formats)
- WAV, FLAC (lossless formats)
- OGG (open source format)

### FFT Analysis
Real-time frequency analysis for audio visualization.

**Features:**
- Three-band frequency visualization
- Real-time spectrum analysis
- Beat detection and BPM calculation
- Audio feature extraction

## Deployment

### iOS Deployment
1. **Code Signing**: Configure proper code signing certificates
2. **App Store**: Follow Apple's App Store guidelines
3. **TestFlight**: Use TestFlight for beta testing

### Android Deployment
1. **Signing**: Generate and configure release signing keys
2. **Play Store**: Follow Google Play Store policies
3. **Internal Testing**: Use Google Play Console for testing

## Troubleshooting

### Common Issues

#### Build Errors
- **Metro Cache**: Clear Metro cache with `npx react-native start --reset-cache`
- **Node Modules**: Delete node_modules and reinstall dependencies
- **iOS Pods**: Clean and reinstall CocoaPods dependencies

#### Audio Issues
- **Permissions**: Ensure proper audio permissions are granted
- **Native Modules**: Verify native audio modules are properly linked
- **File Formats**: Check that audio files are in supported formats

#### BLE Connection Issues
- **Permissions**: Verify Bluetooth permissions are granted
- **Device Compatibility**: Ensure device supports BLE
- **Range**: Check device is within Bluetooth range

### Debug Mode
The app includes debug features for development:
- BLE connection status overlay
- Audio processing diagnostics
- Memory usage monitoring
- Performance metrics

## How to Debug

### Setting Up Debug Environment
1. **Enable Debug Mode**: Set `DEBUG=true` in your `.env` file or app config
2. **React Native Debugger**: Install and run React Native Debugger
   ```bash
   npm install -g react-native-debugger
   react-native-debugger
   ```
3. **Flipper**: For advanced debugging, install Flipper and enable plugins
   ```bash
   npm install --save-dev react-native-flipper
   ```

### Debugging Techniques
- **Console Logs**: Use `console.log()` for basic debugging
- **React DevTools**: Inspect component hierarchy and state
- **Network Inspector**: Monitor API calls and BLE communication
- **Performance Monitoring**: Use Flipper's performance plugin
- **BLE Debugging**: Enable BLE logs in the app settings

### Common Debug Commands
```bash
# Clear Metro cache
npx react-native start --reset-cache

# Run with verbose logging
npx react-native run-android --verbose

# iOS device logs
xcrun simctl spawn booted log stream --level debug

# Android device logs
adb logcat | grep ReactNative
```

### Troubleshooting Audio Issues
- Check audio file permissions
- Verify native module linking
- Test with different audio formats
- Monitor memory usage during playback

### BLE Debugging
- Enable Bluetooth debugging in Android settings
- Use nRF Connect app for BLE packet inspection
- Check device pairing status
- Monitor connection stability

## How to Make APK

### Prerequisites
- Android Studio installed
- JDK 11 or higher
- Android SDK with API level 21+
- Signing keys configured

### Building Release APK
1. **Configure Signing**:
   Create `android/app/keystore.properties`:
   ```
   storePassword=your_store_password
   keyPassword=your_key_password
   keyAlias=your_key_alias
   storeFile=../keystore.jks
   ```

2. **Generate Keystore** (if not exists):
   ```bash
   keytool -genkeypair -v -storetype PKCS12 -keystore keystore.jks -alias lychee-key -keyalg RSA -keysize 2048 -validity 10000
   ```

3. **Build APK**:
   ```bash
   cd android
   ./gradlew assembleRelease
   ```

4. **Locate APK**:
   The APK will be generated at `android/app/build/outputs/apk/release/app-release.apk`

### Building Debug APK
```bash
cd android
./gradlew assembleDebug
```
Debug APK: `android/app/build/outputs/apk/debug/app-debug.apk`

### Using Android Studio
1. Open project in Android Studio
2. Select "Build" > "Generate Signed Bundle/APK"
3. Choose APK, select release build variant
4. Configure signing if not done
5. Build and locate APK

### Testing APK
- Install on test device: `adb install app-release.apk`
- Test all features, especially BLE and audio
- Verify permissions and functionality

## Contributing

### Workflow
1. **Feature Branches**: Create feature branches from `main`
2. **Pull Requests**: Submit PRs for code review
3. **Testing**: Ensure all tests pass before merging
4. **Documentation**: Update documentation for new features

### Branch Strategy
- `main`: Development branch with latest features
- `stable-ui-version`: Production-ready releases
- `feature/*`: Feature development branches
- `hotfix/*`: Critical bug fixes

## Scripts

```bash
# Development
npm start                    # Start Metro bundler
npm run ios                  # Run on iOS simulator
npm run android              # Run on Android emulator

# Code Quality
npm run lint                 # Run ESLint
npm run test                 # Run Jest tests

# Utilities
npm run clean                # Clean build artifacts
```

## Environment Variables

Create a `.env` file in the root directory:
```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
API_BASE_URL=https://api.lychee.inc
```

## License

© 2025 Lychee Inc. All rights reserved.
