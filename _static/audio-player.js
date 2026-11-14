(function () {
  function formatTime(seconds) {
    if (!Number.isFinite(seconds)) return "0:00";
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60).toString().padStart(2, "0");
    return `${mins}:${secs}`;
  }

  function initAudioCard(card) {
    if (card.dataset.initialized === "true") return;
    card.dataset.initialized = "true";

    const audio = card.querySelector(".audio-el");
    const chapterSelect = card.querySelector(".chapter-select");
    const prevButton = card.querySelector(".prev-chapter");
    const nextButton = card.querySelector(".next-chapter");
    const speedSelect = card.querySelector(".speed-select");
    const volumeSlider = card.querySelector(".volume-slider");
    const timeDisplay = card.querySelector(".time-display");

    if (!audio || !chapterSelect) return;

    function getChapters() {
      return Array.from(chapterSelect.options)
        .map(option => Number(option.value))
        .filter(value => Number.isFinite(value));
    }

    function getCurrentChapterIndex() {
      const chapters = getChapters();
      let index = 0;

      for (let i = 0; i < chapters.length; i++) {
        if (audio.currentTime >= chapters[i]) index = i;
      }

      return index;
    }

    function seekToChapter(index, shouldPlay) {
      const chapters = getChapters();
      if (chapters.length === 0) return;

      const safeIndex = Math.max(0, Math.min(index, chapters.length - 1));
      audio.currentTime = chapters[safeIndex];
      chapterSelect.selectedIndex = safeIndex;

      if (shouldPlay) {
        audio.play().catch(function () {
          /* Browser may block autoplay; ignore safely. */
        });
      }
    }

    function updateTime() {
      chapterSelect.selectedIndex = getCurrentChapterIndex();

      if (timeDisplay) {
        timeDisplay.textContent = `${formatTime(audio.currentTime)} / ${formatTime(audio.duration)}`;
      }
    }

    chapterSelect.addEventListener("change", function () {
      const selectedTime = Number(chapterSelect.value);

      if (Number.isFinite(selectedTime)) {
        audio.currentTime = selectedTime;
        audio.play().catch(function () {
          /* Browser may block autoplay; ignore safely. */
        });
      }
    });

    if (prevButton) {
      prevButton.addEventListener("click", function () {
        const chapters = getChapters();
        const index = getCurrentChapterIndex();

        if (chapters.length === 0) return;

        if (audio.currentTime - chapters[index] > 3) {
          seekToChapter(index, true);
        } else {
          seekToChapter(index - 1, true);
        }
      });
    }

    if (nextButton) {
      nextButton.addEventListener("click", function () {
        seekToChapter(getCurrentChapterIndex() + 1, true);
      });
    }

    if (speedSelect) {
      audio.playbackRate = Number(speedSelect.value) || 1;

      speedSelect.addEventListener("change", function () {
        audio.playbackRate = Number(speedSelect.value) || 1;
      });
    }

    if (volumeSlider) {
      audio.volume = Number(volumeSlider.value);

      volumeSlider.addEventListener("input", function () {
        audio.volume = Number(volumeSlider.value);
      });
    }

    audio.addEventListener("loadedmetadata", updateTime);
    audio.addEventListener("timeupdate", updateTime);
    updateTime();
  }

  function initAllAudioCards() {
    document.querySelectorAll(".audio-card").forEach(initAudioCard);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllAudioCards);
  } else {
    initAllAudioCards();
  }
})();

