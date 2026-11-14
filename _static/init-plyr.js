// Waits for the JupyterBook page to load, then upgrades the audio players
document.addEventListener('DOMContentLoaded', () => {
    const players = Plyr.setup('.plyr', {
        controls: ['play', 'progress', 'current-time', 'mute', 'volume'],
        // You can change the main player color by adding a custom CSS variable later!
    });
});