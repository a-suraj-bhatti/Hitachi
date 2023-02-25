import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class BookingTest {
    public static void main(String[] args) {

        WebDriver driver = new ChromeDriver();

        // Navigate to the Booking.com website
        driver.get("https://www.booking.com/");
        driver.findElement(By.xpath("//button[@data-ui-sr='location_input_from_0']")).click();
        driver.findElement(By.xpath("//span[@class='Icon-module__root___0jUKs css-lyj9ft Icon-module__root--size-small___AvlR0']//*[name()='svg']")).click();
        driver.findElement(By.xpath("//input[@placeholder='Airport or city']")).sendKeys("Delhi");
        driver.findElement(By.xpath("//b[text()='DEL']")).click();
        driver.findElement(By.xpath("//button[@aria-describedby='location_input_to_0_error']")).click();
        driver.findElement(By.xpath("//input[@placeholder='Airport or city']")).sendKeys("Bangalore");
        driver.findElement(By.xpath("//b[text()='BLR']")).click();
        driver.findElement(By.xpath("//button[@placeholder='Choose departure date']")).click();
        LocalDate futureDate = LocalDate.now().plusDays(5);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d MMMM yyyy");
        String formattedDate = futureDate.format(formatter);
        String xpathExpression = "//span[@aria-label='<<text_replace>>']";
        driver.findElement(By.xpath(xpathExpression.replace("<<text_replace>>", formattedDate);)).click();
        driver.findElement(By.xpath("//span[text()='Search']")).click();
      WebDriverWait wait = new WebDriverWait(driver, explicitWait);
        wait.until(ExpectedConditions.invisibilityOfElementLocated("//div[contains(text(),'Look out for flexible ticket options...')]"));
        driver.findElement(By.xpath("//button[@data-testid='search_tabs_CHEAPEST']")).click();
        driver.findElement(By.xpath("//button[@aria-describedby='flight-card-0']")).click();
        driver.findElement(By.xpath("//span[normalize-space()='Select']")).click();

        driver.quit();
    }
}
