package zalando.analytics.annotation.transfer;

import zalando.analytics.base.Language;
import zalando.analytics.base.Sentence;
import zalando.analytics.corpus.ConllFileReader;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CpacGetAlignments {

    private static final Logger log = LogManager.getLogger(AnnotationTransfer.class);

    public void getAlignments(int corpusSize, String idPattern, String heuristicLang, String fileLang1, String fileLang2, String outputFile) {

        Pattern regex = Pattern.compile(pattern);

        HeuristicAligner aligner;
        if (heuristicLang.equals("fr")) {
            aligner = HeuristicAligner.getInstance(Language.FRENCH);
        } else if (heuristicLang.equals("ar")) {
            aligner = HeuristicAligner.getInstance(Language.ARABIC);
        }

        // Reading cupt files
        ConllFileReader conllFileReaderLang1 = ConllFileReader
                .readFromFile(fileLang1).splitByTabsOnly();
        ConllFileReader conllFileReaderLang2 = ConllFileReader
                .readFromFile(fileLang2).splitByTabsOnly();

        // Sentence list creation
        List<Sentence> sentencesLang1 = conllFileReaderLang1.readSentences(corpusSize);
        List<Sentence> sentencesLang2 = conllFileReaderLang2.readSentences(corpusSize);

        if (sentencesLang1.size() == corpusSize && sentencesLang2.size() == corpusSize) {
            log.info("Corpus size: OK");
        } else {
            log.info("Corpus size: NOT OK");
            log.info("CORPUS SIZE : " + corpusSize);
            log.info("L1 SENTENCES : " + sentencesLang1.size());
            log.info("L2 SENTENCES : " + sentencesLang2.size());
        }

        List<String> alignments = new ArrayList<>();

        // Retrieving alignments for each Lang1/Lang2 pair
        for (int i = 0; i < sentencesLang1.size(); ++i) {
            // Use this if condition when last lines don't 'want' to be written
            /*if (i < 181) {
                continue;
            }*/
            Sentence sourceSentence = sentencesLang1.get(i);
            Sentence targetSentence = sentencesLang2.get(i);

            BiSentence biSentence = new BiSentence(sourceSentence, targetSentence);
            biSentence.align(aligner);

            String idPhrase = null;
            List<String> metadata = sourceSentence.getMetadata();
            for (String metadatum : metadata) {
                Matcher matcher = regex.matcher(metadatum);
                if (matcher.find()) {
                    idPhrase = matcher.group(0).substring(2);
                }
            }
            // In case there are missing sentences in output file, use this and copy/paste in file
            log.info(idPhrase + "\t" + biSentence.aligments);

            if (biSentence.aligments.isEmpty()) {
                alignments.add(idPhrase + "\t" + "{EMPTY}");
            } else {
                alignments.add(idPhrase + "\t" + biSentence.aligments.toString());
            }
        }

        if (alignments.size() == corpusSize) {
            log.info("Alignments size: OK");
        } else {
            log.info("Alignments size: NOT OK");
            log.info("ALIGNMENTS CORPUS: " + alignments.size()
                    + " instead of " + corpusSize);
        }
        
        // Writing retrieved alignments in file
        try {
            File myObj = new File(outputFile); // update path
            if (myObj.createNewFile()) {
                log.info("File created: " + myObj.getName());
            } else {
                log.info("File already exists.");
            }
            FileWriter myWriter = new FileWriter(outputFile); // update path
            for (String alignment : alignments) {
                myWriter.write(alignment + "\n");
            }
            log.info("Done with alignments.");
        } catch (IOException e) {
            log.info("An error occurred.");
            e.printStackTrace();
        }   
    }

    public static void main(String[] args) {
        getAlignments(0, "\:\:\d{1,5}", "fr", "fr", "en", "my/output/file/path")
    }
}
