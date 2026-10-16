import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { titelFont } from "./fonts";

// Test of renderen werkt: lokaal lettertype, afbeelding uit public/, spring-animatie.
const fontFamily = titelFont;

export const Haalbaarheid: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const pop = spring({ frame, fps, config: { damping: 12 } });
  const tekst = interpolate(frame, [20, 35], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#fffaf7",
        justifyContent: "center",
        alignItems: "center",
        fontFamily,
      }}
    >
      <Img src={staticFile("logo-icon.png")} style={{ width: 480, transform: `scale(${pop})` }} />
      <div
        style={{
          marginTop: 60,
          fontSize: 72,
          fontWeight: 700,
          color: "#c8105a",
          opacity: tekst,
        }}
      >
        render-test ok
      </div>
    </AbsoluteFill>
  );
};
