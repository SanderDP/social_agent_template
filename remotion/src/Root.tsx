import { Composition } from "remotion";
import { Haalbaarheid } from "./Haalbaarheid";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Haalbaarheid"
      component={Haalbaarheid}
      durationInFrames={90}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
